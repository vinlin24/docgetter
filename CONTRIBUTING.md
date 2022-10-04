# Contributing

After forking my repository:

```shell
git clone https://github.com/USERNAME/docgetter.git
cd docgetter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements_dev.txt
pip install -e .
```

To version bump, update **both** the `metadata.version` value in [setup.cfg](setup.cfg#L3) and the `__version__` variable in [\_\_init\_\_.py](src/docgetter/__init__.py). Update any metadata and documentation *before* building!

To build the project source, I provided an [overgrown script](scripts/build.py):

```shell
python scripts/build.py
```

Issues, pull requests, and feature proposals are all welcome!
