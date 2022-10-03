"""build.py

Script for building the project source into a distributable whl file.
"""

import os
import subprocess
import sys
from pathlib import Path


def AbsPath(relative: str) -> Path:
    """Convert a relative path string to a resolved absolute Path."""
    return (Path(__file__).parent / relative).resolve()


VENV_PATH = AbsPath("../.venv")
"""Virtual environment for the project."""

DIST_PATH = AbsPath("../dist")
"""Directory of the the final whl distribution file."""

TEMP_PATH = AbsPath("../build")
"""Directory to hold temporary files as part of bdist_wheel."""


def box_print(*args, **kwargs) -> None:
    """Print a line surrounded by dashes spanning the terminal width."""
    width, _ = os.get_terminal_size()
    print("-" * width)
    print(*args, **kwargs)
    print("-" * width)


# Assert that the script is being run in the project's virtual environment
if sys.prefix != str(VENV_PATH):
    box_print("ABORTED: Activate the project virtual environment first.")
    sys.exit(1)

command = (
    f"\"{sys.executable}\" setup.py bdist_wheel "
    f"--dist-dir \"{DIST_PATH}\" "
    f"--bdist-dir \"{TEMP_PATH}\""
)

# Echo
box_print(command)

# Run
subprocess.run(command, check=True)

box_print("Successfully built project source.")
