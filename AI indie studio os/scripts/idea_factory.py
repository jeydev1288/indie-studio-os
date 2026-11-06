"""Validate a local JSON array of ideas and flag exact duplicate candidates.

No network access or file modification is performed. A matching pair is a
candidate for human review, not an automatic decision to merge records.
"""
import argparse
from datetime import date
import json
from pathlib import Path
from urllib.parse import urlsplit

SCORE_KEYS = ('severity', 'access', 'gap', 'feasibility', 'willingness')


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _valid_url(value):
    if not _text(value):
        return False
    try:
        parsed = urlsplit(value)
        return (parsed.scheme in ('http', 'https') and bool(parsed.hostname)
                and not parsed.username and not parsed.password and not any(c.isspace() for c in value))
    except ValueError:
        return False


def validate_records(records):
    if not isinstance(records, list):
        return ['root must be a JSON array']
    errors, ids = [], set()
    for i, record in enumerate(records):
        loc = f'[{i}]'
        if not isinstance(record, dict):
            errors.append(f'{loc} must be an object')
            continue
        for key in ('id', 'title', 'customer', 'problem'):
            if not _text(record.get(key)):
                errors.append(f'{loc}.{key} must be nonempty text')
        ident = record.get('id')
        if _text(ident):
            normalized_id = ident.strip().casefold()
            if normalized_id in ids:
                errors.append(f'{loc}.id duplicates an earlier ID')
            ids.add(normalized_id)
        hypotheses = record.get('hypotheses')
        if not isinstance(hypotheses, list) or not all(_text(h) for h in hypotheses):
            errors.append(f'{loc}.hypotheses must be an array of nonempty strings')
        facts = record.get('facts')
        if not isinstance(facts, list):
            errors.append(f'{loc}.facts must be an array')
        else:
            for j, fact in enumerate(facts):
                floc = f'{loc}.facts[{j}]'
                if not isinstance(fact, dict):
                    errors.append(f'{floc} must be an object')
                    continue
                if not _text(fact.get('claim')):
                    errors.append(f'{floc}.claim must be nonempty text')
                if not _valid_url(fact.get('url')):
                    errors.append(f'{floc}.url must be an http(s) URL')
                checked = fact.get('checked_at')
                try:
                    if not isinstance(checked, str) or date.fromisoformat(checked).isoformat() != checked:
                        raise ValueError
                except ValueError:
                    errors.append(f'{floc}.checked_at must be a valid YYYY-MM-DD date')
        scores = record.get('scores')
        if not isinstance(scores, dict):
            errors.append(f'{loc}.scores must be an object')
        else:
            for key in SCORE_KEYS:
                if key not in scores or (scores[key] is not None and
                    (type(scores[key]) is not int or not 1 <= scores[key] <= 5)):
                    errors.append(f'{loc}.scores.{key} must be an integer 1-5 or null')
    return errors


def _normalize(value):
    return ' '.join(value.casefold().split())


def find_duplicates(records):
    candidates = []
    for i, left in enumerate(records):
        for right in records[i + 1:]:
            reasons = []
            if _normalize(left['title']) == _normalize(right['title']):
                reasons.append('title')
            if (_normalize(left['customer']), _normalize(left['problem'])) == (
                    _normalize(right['customer']), _normalize(right['problem'])):
                reasons.append('customer+problem')
            if reasons:
                candidates.append({'ids': [left['id'], right['id']], 'matches': reasons})
    return candidates


def main():
    parser = argparse.ArgumentParser(description='Read-only local idea validation; no URL fetching.')
    parser.add_argument('path', type=Path, help='JSON array of idea records')
    args = parser.parse_args()
    try:
        records = json.loads(args.path.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(json.dumps({'errors': [str(exc)]}, ensure_ascii=True))
        return 2
    errors = validate_records(records)
    if errors:
        print(json.dumps({'errors': errors}, ensure_ascii=True, indent=2))
        return 1
    print(json.dumps({'valid_count': len(records), 'duplicate_candidates': find_duplicates(records)},
                     ensure_ascii=True, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
