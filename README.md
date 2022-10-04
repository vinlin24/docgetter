# docgetter

![Python version requirement](https://img.shields.io/badge/Python-3.7%2B-blue)

## Quick Start

docgetter is a command line shortcut for opening Python documentation webpages:

```shell
docs argparse
docs --pypi discord.py
docs --readthedocs array --search
```

## Description

Suppose you're dutifully coding in your editor of choice and you have to look something up *really quick*. You've probably already mastered the art of Alt-Tabbing, but the documentation is still clicks away, not to mention that if it's not already open, you have to search on Google and *actually use the mouse* to open links (*shudders*). However, you always have a terminal open, so your hands never leave the keyboard.

This program currently supports three documentation websites:

1. [docs.python.org](https://docs.python.org/3/) for the Python standard library. [↓](#1-python-standard-library)
2. [PyPI](https://pypi.org/) project homepages for packages available on PyPI. [↓](#2-pypi-project-homepage)
3. [readthedocs.io](https://readthedocs.org/) homepages for projects that host their documentation on readthedocs.io. [↓](#3-readthedocsio-project-homepage)

## Installation

<table>
<tr>
    <th>Windows</th>
    <th>Unix/MacOS</th>
</tr>
<tr>
<td>

```
py -m pip install docgetter
```

</td>
<td>

```
python3 -m pip install docgetter
```

</td>
</tr>
</table>

There are no dependencies, just pure standard library! It is OS-independent, but browser behavior may vary depending on your browser of choice as determined by the underlying [webbrowser](https://docs.python.org/3/library/webbrowser.html) module.

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

This tool is very simple, but I made it because it provides a shortcut to something I find myself doing very often as someone constantly bouncing between doc pages. I hope someone else finds it useful too!
