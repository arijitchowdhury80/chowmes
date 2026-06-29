import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
HELPER = REPO_ROOT / "tools" / "hostinger-vps-ssh" / "scripts" / "ssh-hermes-vps"
TOP_LEVEL_HELPER = REPO_ROOT / "scripts" / "chowmes-ssh-helper"


class HostingerVpsSshHelperTests(unittest.TestCase):
    def make_env(self, root: Path, *, port: str = "2222") -> Path:
        key = root / "key"
        key.write_text("not-a-real-key\n")
        key.chmod(0o600)
        env_file = root / ".env.local"
        env_file.write_text(
            "\n".join(
                [
                    "SSH_HOST=127.0.0.1",
                    "SSH_USER=chowmesadmin",
                    f"SSH_KEY={key}",
                    f"SSH_PORT={port}",
                ]
            )
            + "\n"
        )
        return env_file

    def test_uses_ssh_port_and_identities_only_for_key_auth(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_file = self.make_env(root, port="2222")
            fake_bin = root / "bin"
            fake_bin.mkdir()
            calls = root / "calls.txt"
            ssh = fake_bin / "ssh"
            ssh.write_text(
                textwrap.dedent(
                    f"""\
                    #!/bin/sh
                    printf '%s\\n' "$*" > {calls}
                    exit 0
                    """
                )
            )
            ssh.chmod(0o755)
            env = os.environ.copy()
            env["PATH"] = f"{fake_bin}:{env['PATH']}"

            result = subprocess.run(
                [str(HELPER), "--env", str(env_file), "hostname"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env=env,
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            call = calls.read_text()
            self.assertIn("-p 2222", call)
            self.assertIn("-o IdentitiesOnly=yes", call)
            self.assertIn("chowmesadmin@127.0.0.1", call)

    def test_diagnose_reports_safe_connection_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_file = self.make_env(root, port="22")

            result = subprocess.run(
                [str(HELPER), "--env", str(env_file), "--diagnose"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("ssh_diagnose_host_present=yes", result.stdout)
            self.assertIn("ssh_diagnose_user=chowmesadmin", result.stdout)
            self.assertIn("ssh_diagnose_port=22", result.stdout)
            self.assertIn("ssh_diagnose_key_exists=yes", result.stdout)
            self.assertIn("ssh_diagnose_tcp_status=", result.stdout)
            self.assertNotIn("not-a-real-key", result.stdout)

    def test_connection_refused_message_names_pre_auth_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_file = self.make_env(root)
            fake_bin = root / "bin"
            fake_bin.mkdir()
            ssh = fake_bin / "ssh"
            ssh.write_text(
                "#!/bin/sh\n"
                "echo 'ssh: connect to host 127.0.0.1 port 2222: Connection refused' >&2\n"
                "exit 255\n"
            )
            ssh.chmod(0o755)
            env = os.environ.copy()
            env["PATH"] = f"{fake_bin}:{env['PATH']}"

            result = subprocess.run(
                [str(HELPER), "--env", str(env_file), "hostname"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env=env,
            )

            self.assertEqual(result.returncode, 255, result.stdout)
            self.assertIn("Connection refused", result.stdout)
            self.assertIn("TCP connection was refused before SSH authentication", result.stdout)
            self.assertIn("Host, user, and key were not tested by the server", result.stdout)

    def test_chowmes_wrapper_prefers_workspace_helper_before_global_helper(self):
        text = TOP_LEVEL_HELPER.read_text()

        workspace_check = 'if [ -x "$workspace_helper" ]; then'
        global_check = 'if [ -x "$codex_helper" ]; then'
        self.assertIn(workspace_check, text)
        self.assertIn(global_check, text)
        self.assertLess(text.index(workspace_check), text.index(global_check))


if __name__ == "__main__":
    unittest.main()
