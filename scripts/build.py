"""build.py

Script for building the project source into a distributable whl file.
"""

import os
import re
import subprocess
import sys
from configparser import ConfigParser
from pathlib import Path


def AbsPath(relative: str) -> Path:
    """Convert a relative path string to a `resolve()`d absolute Path.

    The relative path is interpreted as relative to the location of
    this script i.e. the directory part of `__file__`, NOT the current
    working directory. This way, this script can be invoked from any
    working directory.
    """
    return (Path(__file__).parent / relative).resolve()


VENV_PATH = AbsPath("../.venv")
"""Virtual environment for the project."""

DIST_PATH = AbsPath("../dist")
"""Directory of the the final whl distribution file."""

TEMP_PATH = AbsPath("../build")
"""Directory to hold temporary files as part of bdist_wheel."""

CFG_PATH = AbsPath("../setup.cfg")
"""Project setup.cfg file."""

SEMVER_MATCHER = re.compile(
    r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-]["
    r"0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-"
    r"9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?"
)
"""
Regex matcher for semantic version labels.
Using the second regex provided on: https://semver.org/.
"""


def box_print(*args, **kwargs) -> None:
    """Print a line surrounded by dashes spanning the terminal width."""
    width, _ = os.get_terminal_size()
    print("-" * width)
    print(*args, **kwargs)
    print("-" * width)


def validate_version() -> str:
    """Extract, validate, and return the version from setup.cfg.

    Abort script if any of the following, checked in order, are true:
    - metadata.version matches the version of the existing distribution.
    - metadata.version is not compliant with semantic versioning.
    - metadata.version does not match __version__.
    """
    config = ConfigParser()
    config.read(CFG_PATH)
    # A KeyError means you didn't even get your setup.cfg right
    # pylint: disable-next=redefined-outer-name
    version = config["metadata"]["version"]

    # Abort: metadata.version matches the version of an existing distribution
    # pylint: disable-next=redefined-outer-name
    for path in DIST_PATH.iterdir():
        if version in path.name:
            box_print(
                f"ABORTED: The current distribution {path} already has "
                f"metadata.version={version!r}."
            )
            sys.exit(1)

    # Abort: metadata.version is not compliant with semantic versioning
    if SEMVER_MATCHER.match(version) is None:
        box_print(
            f"ABORTED: metadata.version={version!r} is not SemVer compliant!"
        )
        sys.exit(1)

    try:
        # pylint: disable-next=import-outside-toplevel
        from docgetter import __version__
    except ImportError as e:
        raise e.__class__("Try running: pip install -e .")

    # Abort: metadata.version does not match __version__
    if version != __version__:
        box_print(
            f"ABORTED: __version__={__version__!r} does not match "
            f"metadata.version={version!r}."
        )
        sys.exit(1)

    return version


# Assert that the script is being run in the project's virtual environment
if sys.prefix != str(VENV_PATH):
    box_print("ABORTED: Activate the project virtual environment first.")
    sys.exit(1)

# Remind and prompt for confirmation
confirmation = input(
    "Did you update all relevant documentation and metadata? (y/N) "
)
if confirmation.lower() != "y":
    sys.exit(1)

# Make sure I'm not being an idiot
version = validate_version()

# Set up the actual command to run
command = (
    f"\"{sys.executable}\" setup.py bdist_wheel "
    f"--dist-dir \"{DIST_PATH}\" "
    f"--bdist-dir \"{TEMP_PATH}\""
)

# Prepare to delete current dist(s) if build succeeds
current_dists = list(DIST_PATH.iterdir())

# Echo
box_print(command)

# Run
subprocess.run(command, check=True)

# Report
box_print(f"Successfully built version {version}.")

# Cleanup
for path in current_dists:
    path.unlink()
