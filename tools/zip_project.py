import os
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT = BASE_DIR / "portfolio_app.zip"

def include(path: Path) -> bool:
    # Exclude venvs, __pycache__, .git and compiled/binaries
    excluded_dirs = {".git", ".venv", "venv", "__pycache__", ".mypy_cache", ".pytest_cache"}
    parts = set(path.parts)
    if parts & excluded_dirs:
        return False
    # Exclude media files users might upload locally
    if path.is_file() and path.suffix.lower() in {".pyc", ".pyo", ".so", ".dll"}:
        return False
    return True

def main():
    if OUTPUT.exists():
        OUTPUT.unlink()
    root_dir = str(BASE_DIR)
    base_name = str(OUTPUT.with_suffix(""))
    shutil.make_archive(base_name, "zip", root_dir=root_dir, base_dir=".")
    print(f"Created {OUTPUT}")

if __name__ == "__main__":
    main()