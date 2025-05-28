from pathlib import Path
import subprocess
import sys
import venv

venv.create("venv", clear=True, with_pip=True)
if sys.platform == "win32":
    python_file = Path("venv", "Scripts", "python.exe")
else:
    python_file = Path("venv", "bin", "python")
subprocess.Popen([python_file, "-m", "pip", "install", "PyGithub"])
subprocess.Popen([python_file, Path( "_scripts", "repository.py")])
print(f"{python_file=}")
