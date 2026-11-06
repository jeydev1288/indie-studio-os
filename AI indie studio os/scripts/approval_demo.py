"""Approval interaction demonstration only; no external actions are executed."""

import argparse

ACTIONS = ("deploy", "paid_api", "delete_data", "send_message", "permissions")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=ACTIONS)
    action = parser.parse_args().action
    try:
        response = input(f"MOCK ONLY: type CONFIRM {action} to simulate approval: ")
    except EOFError:
        response = ""
    if response != f"CONFIRM {action}":
        print("MOCK_BLOCKED")
        return 1
    print(f"MOCK_EXECUTED {action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
