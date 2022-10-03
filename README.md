# docgetter

**Command line shortcut for opening Python documentation webpages.** 

## Quick Start

```console
docs argparse
docs --pypi discord.py
docs --readthedocs google --search
```

See [below](#examples) for more examples.

## Description

Suppose you're dutifully coding in your editor of choice and you have to look something up *really quick*. You've probably already mastered the art of Alt-Tabbing, but the documentation is still clicks away, not to mention that if it's not already open, you have to search on Google and *actually use the mouse* to open links (*shudders*). On the other hand, you always have a terminal open, so your hands never leave the keyboard.

This program currently supports three documentation websites:

1. [docs.python.org](https://docs.python.org/3/) for the Python standard library. [↓](#1-python-standard-library)
2. [PyPI](https://pypi.org/) project homepages for packages available on PyPI. [↓](#2-pypi-project-homepage)
3. [readthedocs.io](https://readthedocs.org/) homepages for projects that host their documentation on readthedocs.io. [↓](#3-readthedocsio-project-homepage)

I hope you find this simple tool useful! It certainly helps someone like me who always bounces between doc pages. Personally, I'm [trying to become a coding ninja](https://gist.github.com/vinlin24/0bc08034d84bb604286b29d69c04d3f8), and clicking things on Google becomes an annoying chore very quickly.

## Installation

This package is not yet available on to PyPI, but I plan to upload it soon!

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

By default, the supplied name is interpreted as a Python standard library module/package. You can use the (mutually exclusive) `-p`/`--pypi` or `-r`/`--readthedocs` flags to specify that the name refers to a PyPI project or readthedocs.io homepage respectively instead.

You can also add the global `-s/--search` flag with any of these methods to specify using the site's search engine instead of attempting to directly load a URL.

## Examples

### (1) Python Standard Library

```console
docs pathlib        # Directly load pathlib's docs page
docs -s path        # Search for "path" on docs.python.org
```

### (2) PyPI Project Homepage

```console
docs -p numpy           # Directly load numpy's PyPI homepage
docs --pypi pandas      # Directly load pandas' PyPI homepage
docs -sp spotify        # Search "spotify" on pypi.org
```

### (3) readthedocs.io Project Homepage

```console
docs -r selenium-python     # Directly load selenium's docs page
docs --readthedocs rich     # Directly load rich's docs page
docs -rp youtube            # Search "youtube" on readthedocs.io
```
