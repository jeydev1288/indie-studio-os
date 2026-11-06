import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from idea_factory import validate_records, find_duplicates


def idea():
    return {'id': 'I-1', 'title': 'Task Helper', 'customer': 'indie developer',
            'problem': 'misses tasks', 'hypotheses': ['May save time'],
            'facts': [{'claim': 'a documented feature', 'url': 'https://example.org/page',
                       'checked_at': '2026-11-06'}],
            'scores': {'severity': 3, 'access': None, 'gap': 2, 'feasibility': 4, 'willingness': None}}


class IdeaFactoryTests(unittest.TestCase):
    def test_valid_and_nullable_scores(self):
        self.assertEqual(validate_records([idea()]), [])

    def test_invalid_source_date_and_scores(self):
        for key, val in [('url', ''), ('checked_at', '2026-02-30')]:
            entry = idea(); entry['facts'][0][key] = val
            self.assertTrue(validate_records([entry]), key)
        for score in [0, 6, True, 2.5]:
            entry = idea(); entry['scores']['severity'] = score
            self.assertTrue(validate_records([entry]), score)

    def test_duplicate_ids_and_match_candidates(self):
        first = idea(); second = copy.deepcopy(first); second['id'] = 'I-2'
        second['title'] = '  TASK   HELPER  '
        self.assertEqual(len(find_duplicates([first, second])), 1)
        second['title'] = 'Other'; self.assertEqual(len(find_duplicates([first, second])), 1)
        second['id'] = 'I-1'; self.assertTrue(validate_records([first, second]))

    def test_cli_invalid_exits_nonzero_without_modifying_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'ideas.json'; entry = idea(); entry['facts'][0]['url'] = ''
            data = json.dumps([entry]); path.write_text(data, encoding='utf-8')
            proc = subprocess.run([sys.executable, str(ROOT / 'scripts/idea_factory.py'), str(path)],
                                  capture_output=True, text=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertEqual(path.read_text(encoding='utf-8'), data)

    def test_cli_reports_candidates_on_valid_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'ideas.json'
            first = idea(); second = copy.deepcopy(first); second['id'] = 'I-2'
            path.write_text(json.dumps([first, second]), encoding='utf-8')
            proc = subprocess.run([sys.executable, str(ROOT / 'scripts/idea_factory.py'), str(path)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            result = json.loads(proc.stdout)
            self.assertEqual(result['valid_count'], 2)
            self.assertEqual(result['duplicate_candidates'][0]['ids'], ['I-1', 'I-2'])


if __name__ == '__main__':
    unittest.main()
