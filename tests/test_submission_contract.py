from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_required_files_exist():
    required = [
        "README.md",
        "sender.py",
        "receiver.py",
        "aes_socket_utils.py",
        "requirements.txt",
        "report-1page.md",
        "threat-model-1page.md",
        "peer-review-response.md",
    ]
    for item in required:
        assert (REPO_ROOT / item).exists(), f"Thiếu file bắt buộc: {item}"


def test_code_uses_aes_not_des():
    code = "\n".join(
        (REPO_ROOT / path).read_text(encoding="utf-8")
        for path in ["aes_socket_utils.py", "sender.py", "receiver.py"]
    )
    assert "Crypto.Cipher import AES" in code
    assert "Crypto.Cipher import DES" not in code
    assert "DES.new" not in code


def test_readme_has_team_placeholders():
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert "Thành viên 1" in readme
    assert "Thành viên 2" in readme
    assert "KEY_PORT" in readme
    assert "DATA_PORT" in readme
