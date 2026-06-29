import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOUL = REPO_ROOT / "SOUL.md"


class AthenaSoulVoiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SOUL.read_text()

    def test_living_voice_kernel_is_present(self):
        required = [
            "## Living Voice Kernel",
            "What is Arijit actually asking for, underneath the words?",
            "What matters most right now: comfort, truth, decision, action, or proof?",
            "What would a sharp partner say if she was not trying to sound like an assistant?",
            "What is the smallest useful answer that still preserves intelligence?",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)

    def test_failure_voice_contract_is_present(self):
        required = [
            "Blocker: what stopped Athena from doing the work.",
            "Effect: what Arijit should assume did or did not happen.",
            "Next move: what Athena will check, what Arijit must provide, or what will happen automatically.",
            "Never send the same failure twice.",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)


if __name__ == "__main__":
    unittest.main()
