"""parser.py

Define the command line parser for this package.
"""

from argparse import ArgumentParser

from . import __version__

parser = ArgumentParser(
    prog=__package__,
    description="Open the documentation page for a module or package."
)

# Intended usage (one of the three, mutually exclusive):
# ------------------------------------------------------
# Standard library official documentation:
#       docs NAME
# PyPI project homepage:
#       docs --pypi NAME
# readthedocs.io documentation homepage:
#       docs --readthedocs NAME

parser.add_argument("name",
                    help=("name of the module/package; treated by default as "
                          "a Python standard library module - use the -p/-r "
                          "flags to specify alternate documentation sites"))

doc_types = parser.add_mutually_exclusive_group()
doc_types.add_argument("-p", "--pypi",
                       action="store_true",
                       help="open the PyPI homepage for this package")
doc_types.add_argument("-r", "--readthedocs",
                       action="store_true",
                       help="open the readthedocs.io page for this package")

# Global flags:
# -------------
# Print version information, do nothing else, and exit
#       [-v | --version]
# Whether program should use search instead of direct URL:
#       [-s | --search]

parser.add_argument("-v", "--version",
                    action="version",
                    version=f"%(prog)s {__version__}")

parser.add_argument("-s", "--search",
                    action="store_true",
                    help=("whether to use the site's search function instead "
                          "of attempting to directly load a URL"))
