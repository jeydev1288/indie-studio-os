import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "approval_demo.py"


class ApprovalDemoTest(unittest.TestCase):
    def run_demo(self, action, answer):
        return subprocess.run([sys.executable, str(SCRIPT), action], input=answer,
                              capture_output=True, text=True, timeout=5)

    def test_rejection_and_missing_input_never_execute(self):
        for action in ("deploy", "paid_api", "delete_data", "send_message", "permissions"):
            for answer in ("NO\n", "", "yes\n"):
                with self.subTest(action=action, answer=answer):
                    result = self.run_demo(action, answer)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertNotIn("MOCK_EXECUTED", result.stdout)

    def test_only_explicit_action_scoped_mock_confirmation_proceeds(self):
        result = self.run_demo("deploy", "CONFIRM deploy\n")
        self.assertEqual(result.returncode, 0)
        self.assertIn("MOCK_EXECUTED deploy", result.stdout)
        result = self.run_demo("deploy", "CONFIRM paid_api\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("MOCK_EXECUTED", result.stdout)

    def test_unknown_action_is_rejected(self):
        result = self.run_demo("arbitrary", "CONFIRM arbitrary\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("MOCK_EXECUTED", result.stdout)


if __name__ == "__main__":
    unittest.main()
