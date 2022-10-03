"""parser.py

Define the command line parser for this package.
"""

from argparse import ArgumentParser

parser = ArgumentParser(description=(
    "Open the documentation page for a module or package."
))

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
# Mutually exclusive browser opening modes:
#       [[-w | --window] | [-t | --tab]]
# Whether program should use search instead of direct URL:
#       [-s | --search]

open_modes = parser.add_mutually_exclusive_group()
open_modes.add_argument("-w", "--window",
                        action="store_true",
                        help="open the browser in a new window if possible")
open_modes.add_argument("-t", "--tab",
                        action="store_true",
                        help="open the browser in a new tab if possible")

parser.add_argument("-s", "--search",
                    action="store_true",
                    help=("whether to use the site's search function instead "
                          "of attempting to directly load a URL"))
