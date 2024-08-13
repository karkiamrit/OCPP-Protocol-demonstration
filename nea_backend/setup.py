import os
from distutils.text_file import TextFile
from setuptools import setup, find_packages
from pathlib import Path
from importlib import import_module


def _parse_requirements(filename):
    """Return requirements from requirements file."""
    setup_path = Path(__file__).resolve().parent.joinpath(filename)
    requirements = TextFile(filename=str(setup_path)).readlines()
    return [p for p in requirements if "-r" not in p]


NAME = 'nea_backend'
SHORT_DESCRIPTION = "FastAPI Charging Station CMS is a web-based Content Management System designed for managing electric vehicle (EV) charging stations. This project leverages FastAPI and PostgreSQL to provide a robust and scalable solution for handling charging station data, real-time communication with charging units using the OCPP protocol, and user management."
URL = "git@github.com:karkiamrit/OCPP-Protocol-demonstration.git"
AUTHOR = 'Amrit Jung Karki'
EMAIL = 'amrit.karki2073@gmail.com'

try:
    VERSION = import_module(NAME+".app.version").__version__
except Exception as e:
    print("Version information cannot be imported using "
          f"'importlib.import_module' due to {e}.")
    about = dict()
    version_path = Path(__file__).resolve().parent.joinpath(NAME, "app",
                                                            "version.py")
    exec(version_path.read_text(), about)
    VERSION = about["__version__"]

try:
    # Load README as description of package
    with open('README.md', encoding="utf-8") as readme_file:
        LONG_DESCRIPTION = readme_file.read()
except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION

# Requirements
INSTALL_REQUIRED = _parse_requirements(os.path.join("requirements", "base.txt"))
# Optional requirements
DEV_REQUIRED = _parse_requirements(os.path.join("requirements", "dev.txt"))
DOC_REQUIRED = _parse_requirements(os.path.join("requirements", "doc.txt"))

# What packages are optional?
EXTRAS = {"doc": DOC_REQUIRED}


setup(name=NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=EMAIL,
      description=SHORT_DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      url=URL,
      packages=find_packages(include=["nea_backend*"],
                             exclude=["tests*", "scripts*", "docs*"]),
      package_data={NAME: ["data/*", ], },
      install_requires=INSTALL_REQUIRED,
      test_requires=DEV_REQUIRED,
      extras_require=EXTRAS,
      setup_requires=['wheel'])
