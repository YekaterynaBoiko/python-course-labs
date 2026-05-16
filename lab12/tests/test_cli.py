import json
import subprocess
import sys
from pathlib import Path


def run_cli(tmp_path: Path, data, args=None):
    file = tmp_path / "input.json"
    file.write_text(json.dumps(data))

    cmd = [sys.executable, "-m", "src.async_tool", str(file)]
    if args:
        cmd += args

    return subprocess.run(cmd, capture_output=True, text=True)


# 1. Basic execution
def test_cli_basic_execution(tmp_path: Path):
    data = [
        {"id": 1, "delay": 0, "good": True},
        {"id": 2, "delay": 0, "good": True},
    ]

    result = run_cli(tmp_path, data)

    assert result.returncode == 0

    output = json.loads(result.stdout)
    assert len(output) == 2


# 2. Mode behavior (async)
def test_cli_async_mode(tmp_path: Path):
    data = [
        {"id": 1, "delay": 0, "good": True},
        {"id": 2, "delay": 0, "good": True},
    ]

    result = run_cli(tmp_path, data, ["--mode", "async"])

    assert result.returncode == 0

    output = json.loads(result.stdout)
    assert all(x["status"] == "done" for x in output)


# 3. Error without flag
def test_cli_error_without_flag(tmp_path: Path):
    data = [
        {"id": 1, "delay": 0, "good": False},
    ]

    result = run_cli(tmp_path, data)

    assert result.returncode != 0


# 4. Error with continue-on-error
def test_cli_continue_on_error(tmp_path: Path):
    data = [
        {"id": 1, "delay": 0, "good": False},
        {"id": 2, "delay": 0, "good": True},
    ]

    result = run_cli(tmp_path, data, ["--continue-on-error"])

    assert result.returncode == 0

    output = json.loads(result.stdout)

    assert len(output) == 2
    assert any(x["id"] == 1 and x["status"] == "error" for x in output)


# 5. Output structure + order
def test_cli_output_order(tmp_path: Path):
    data = [
        {"id": 10, "delay": 0, "good": True},
        {"id": 20, "delay": 0, "good": True},
        {"id": 30, "delay": 0, "good": True},
    ]

    result = run_cli(tmp_path, data)

    output = json.loads(result.stdout)

    assert [x["id"] for x in output] == [10, 20, 30]