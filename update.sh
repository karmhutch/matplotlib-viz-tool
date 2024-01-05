# This file automates the process of adding a new version of vizkarmhutch to TestPyPI.
# Note: you must have `build` and `twine` already installed.

# generate distribution archives
python3 -m build

# upload distribution archives
python3 -m twine upload --repository testpypi dist/*
