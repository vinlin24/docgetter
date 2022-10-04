# docgetter

**Command line shortcut for opening Python documentation webpages.** 

Requirements:

- Python: 3.7 or above
- Dependencies: None!
- Platform: Independent, but browser behavior may vary depending on your browser of choice as determined by the underlying [webbrowser](https://docs.python.org/3/library/webbrowser.html) module.

## Quick Start

```shell
docs argparse
docs --pypi discord.py
docs --readthedocs google --search
```

See [below](#usage) for usage information.

## Description

Suppose you're dutifully coding in your editor of choice and you have to look something up *really quick*. You've probably already mastered the art of Alt-Tabbing, but the documentation is still clicks away, not to mention that if it's not already open, you have to search on Google and *actually use the mouse* to open links (*shudders*). On the other hand, you always have a terminal open, so your hands never leave the keyboard.

This program currently supports three documentation websites:

1. [docs.python.org](https://docs.python.org/3/) for the Python standard library. [↓](#1-python-standard-library)
2. [PyPI](https://pypi.org/) project homepages for packages available on PyPI. [↓](#2-pypi-project-homepage)
3. [readthedocs.io](https://readthedocs.org/) homepages for projects that host their documentation on readthedocs.io. [↓](#3-readthedocsio-project-homepage)

I hope you find this simple tool useful! It certainly helps someone like me who always bounces between doc pages.

## Installation

### Windows

```
py -m pip install docgetter
```

### Unix/MacOS

```
python3 -m pip install docgetter
```

## Usage

```console
$ docs --help
usage: docgetter [-h] [-p | -r] [-v] [-s] name

Open the documentation page for a module or package.

positional arguments:
  name               name of the module/package; treated by default as a
                     Python standard library module - use the -p/-r flags to
                     specify alternate documentation sites

optional arguments:
  -h, --help         show this help message and exit
  -p, --pypi         open the PyPI homepage for this package
  -r, --readthedocs  open the readthedocs.io page for this package
  -v, --version      show program's version number and exit
  -s, --search       whether to use the site's search function instead of
                     attempting to directly load a URL
```

By default, the supplied name is interpreted as a Python standard library module/package. You can use the `-p`/`--pypi` or `-r`/`--readthedocs` flag to specify that the name refers to a PyPI project or readthedocs.io homepage respectively instead.

You can also add the global `-s/--search` flag with any of these methods to specify using the site's search engine instead of attempting to directly load a URL.

## Examples

### Python Standard Library

```shell
docs pathlib        # Directly load pathlib's docs page
docs -s path        # Search for "path" on docs.python.org
```

### PyPI Project Homepage

```shell
docs -p numpy           # Directly load numpy's PyPI homepage
docs --pypi pandas      # Directly load pandas' PyPI homepage
docs -ps spotify        # Search "spotify" on pypi.org
```

### readthedocs.io Project Homepage

```shell
docs -r selenium-python     # Directly load selenium's docs page
docs --readthedocs rich     # Directly load rich's docs page
docs -rs youtube            # Search "youtube" on readthedocs.io
```

## Contributing

After forking my repository:

```shell
git clone https://github.com/USERNAME/docgetter.git
cd docgetter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_dev.txt
pip install -e .
```

To version bump, update **both** the `metadata.version` value in [setup.cfg](setup.cfg#L3) and the `__version__` variable in [\_\_init\_\_.py](src/docgetter/__init__.py). Do this *before* building!

To build the project source, I provided an [overgrown script](scripts/build.py):

```shell
python scripts/build.py
```

Issues, pull requests, and feature proposals are all welcome!
