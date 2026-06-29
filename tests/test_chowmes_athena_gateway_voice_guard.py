import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME = REPO_ROOT / "scripts" / "chowmes-athena-gateway-voice-guard-runtime"


OLD_PROVIDER_FUNCTION = '''def _gateway_provider_error_reply(text: str) -> str:
    """Map raw provider/API errors to a short user-safe Telegram reply."""
    if _GATEWAY_AUTH_ERROR_RE.search(text):
        return (
            "⚠️ Provider authentication failed. Check the configured credentials; "
            "raw provider details are in the gateway logs."
        )
    if _GATEWAY_PROVIDER_POLICY_RE.search(text):
        return (
            "⚠️ The model provider rejected the request. I kept the raw provider "
            "error out of chat; check gateway logs for details or try rephrasing."
        )
    if _GATEWAY_CREDIT_ERROR_RE.search(text):
        return (
            "Arijit, I’m blocked before I can think: OpenRouter credits are exhausted. "
            "Add credits or switch my provider/model, then message me again. "
            "I’ve kept the raw provider details in the gateway logs."
        )
    if _GATEWAY_RATE_LIMIT_RE.search(text):
        return "⏱️ The model provider is rate-limiting requests. Please wait a moment and try again."
    return (
        "⚠️ The model provider failed after retries. I kept raw provider details "
        "out of chat; check gateway logs for diagnostics."
    )
'''


def gateway_fixture() -> str:
    prefix = textwrap.dedent(
        '''\
        import re
        from typing import Optional

        _GATEWAY_AUTH_ERROR_RE = re.compile("auth")
        _GATEWAY_PROVIDER_POLICY_RE = re.compile("policy")
        _GATEWAY_CREDIT_ERROR_RE = re.compile("credit")
        _GATEWAY_RATE_LIMIT_RE = re.compile("rate")
        _GATEWAY_SECRET_PATTERNS = (
            re.compile("secret"),
        )


        def _redact_gateway_user_facing_secrets(text: str) -> str:
            return str(text or "")


        def _gateway_platform_value(platform):
            return platform


        def _looks_like_gateway_provider_error(text: str) -> bool:
            return "provider" in str(text or "").lower()


        def _sanitize_gateway_final_response(platform, text: str) -> str:
            if not text:
                return text
            if _gateway_platform_value(platform) != "telegram":
                return text

            redacted = _redact_gateway_user_facing_secrets(str(text))
            if _looks_like_gateway_provider_error(redacted):
                return _gateway_provider_error_reply(redacted)
            return redacted


        '''
    )
    suffix = textwrap.dedent(
        '''\


        class GatewayRunner:
            async def _handle_message(self, event):
                is_internal = False
                source = event.source
                elif_branch_placeholder = False
                if elif_branch_placeholder:
                    return None

                # Intercept messages that are responses to a pending /update prompt.
                return "agent"
        '''
    )
    return prefix + OLD_PROVIDER_FUNCTION + suffix


class AthenaGatewayVoiceGuardRuntimeTests(unittest.TestCase):
    def run_runtime(self, path: Path, *args):
        env = os.environ.copy()
        env.update(
            {
                "GATEWAY_RUN_PATH": str(path),
                "PYTHON_BIN": "python3",
            }
        )
        return subprocess.run(
            [str(RUNTIME), *args],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=env,
        )

    def test_check_fails_when_guard_is_missing(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "run.py"
            path.write_text(gateway_fixture())
            result = self.run_runtime(path, "--check")
            self.assertEqual(result.returncode, 2, result.stdout)
            self.assertIn("athena_gateway_voice_guard=missing", result.stdout)
            self.assertIn("athena_gateway_voice_guard_provider_voice=missing", result.stdout)

    def test_apply_patches_fixture_and_creates_backup(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "run.py"
            path.write_text(gateway_fixture())
            result = self.run_runtime(path, "--apply")
            self.assertEqual(result.returncode, 0, result.stdout)
            patched = path.read_text()
            self.assertIn("_ATHENA_CASUAL_GREETING_RE = re.compile(", patched)
            self.assertIn("_ATHENA_ROBOTIC_CASUAL_REPLY_RE = re.compile(", patched)
            self.assertIn("def _athena_casual_greeting_reply(", patched)
            self.assertIn("def _athena_rewrite_robotic_casual_reply(", patched)
            self.assertIn("_athena_casual_greeting_reply(event.text)", patched)
            self.assertIn("_athena_rewrite_robotic_casual_reply(redacted)", patched)
            self.assertIn("the active model route is out of usable balance", patched)
            self.assertNotIn("OpenRouter credits are exhausted", patched)
            self.assertEqual(len(list(Path(temp).glob("run.py.bak.athena-voice-guard-*"))), 1)

            check = self.run_runtime(path, "--check")
            self.assertEqual(check.returncode, 0, check.stdout)
            self.assertIn("athena_gateway_voice_guard=present", check.stdout)

    def test_apply_adds_final_reply_rewrite_for_robotic_casual_answers(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "run.py"
            path.write_text(gateway_fixture())
            result = self.run_runtime(path, "--apply")
            self.assertEqual(result.returncode, 0, result.stdout)
            patched = path.read_text()
            self.assertIn("what(?:'|’)?s on your mind", patched)
            self.assertIn("how can i help", patched)
            self.assertIn("ready when you are", patched)
            self.assertIn("return _athena_casual_greeting_reply(text) or", patched)

    def test_apply_is_idempotent_once_guard_exists(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "run.py"
            path.write_text(gateway_fixture())
            first = self.run_runtime(path, "--apply")
            self.assertEqual(first.returncode, 0, first.stdout)
            second = self.run_runtime(path, "--apply")
            self.assertEqual(second.returncode, 0, second.stdout)
            self.assertIn("athena_gateway_voice_guard_apply=noop", second.stdout)
            self.assertIn("athena_gateway_voice_guard_apply=present", second.stdout)
            self.assertEqual(len(list(Path(temp).glob("run.py.bak.athena-voice-guard-*"))), 1)


if __name__ == "__main__":
    unittest.main()
