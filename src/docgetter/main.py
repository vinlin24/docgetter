"""main.py

CLI entry point.
"""

import webbrowser
from urllib.parse import urlencode

from .parser import parser

# Direct URL templates
PYTHON_DOCS_URL = "https://docs.python.org/3/library/{name}.html"
PYPI_PROJECT_URL = "https://pypi.org/project/{name}"
READTHEDOCS_URL = "https://{name}.readthedocs.io"

# Search URL base endpoints
PYTHON_DOCS_SEARCH = "https://docs.python.org/3/search.html?"
PYPI_PROJECT_SEARCH = "https://pypi.org/search/?"
READTHEDOCS_SEARCH = "https://readthedocs.org/search/?"


def main() -> None:
    """Main driver function."""
    ns = parser.parse_args()
    search_query = {"q": ns.name}

    if ns.pypi:
        if ns.search:
            url = PYPI_PROJECT_SEARCH + urlencode(search_query)
        else:
            url = PYPI_PROJECT_URL.format(name=ns.name)

    elif ns.readthedocs:
        if ns.search:
            url = READTHEDOCS_SEARCH + urlencode(search_query)
        else:
            url = READTHEDOCS_URL.format(name=ns.name)

    else:
        if ns.search:
            search_query.update(heck_keywords="yes", area="default")
            url = PYTHON_DOCS_SEARCH + urlencode(search_query)
        else:
            url = PYTHON_DOCS_URL.format(name=ns.name)

    webbrowser.open(url)


if __name__ == "__main__":
    main()
