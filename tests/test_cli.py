import subprocess
import sys

from first_step import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "first_step", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
