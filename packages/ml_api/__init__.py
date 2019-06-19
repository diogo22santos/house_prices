from packages.regression_model.regression_model.config.config import PACKAGE_ROOT

with open(PACKAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()
