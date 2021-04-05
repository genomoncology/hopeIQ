from os import path, listdir
import re
from pathlib import Path

from setuptools import find_packages, setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    version = Path(package, "__version__.py").read_text()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", version).group(1)


def get_long_description():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
    return long_description


def get_dependency_links():
    links = []
    iiq_path = path.join(path.dirname(__file__), "wheels")

    for item in listdir(iiq_path):
        if item.endswith(".whl"):
            links.append(path.join(iiq_path, item))

    return links


install_requires = [
    "arq==0.19",
    "cryptography==3.1.1",
    "entitykb==21.3.25",
    "httpx==0.16.0",
    "loguru==0.5.3",
    "nameparser==1.0.6",
    "openpyxl==3.0.6",
    "pydantic==1.8.1",
    "pyyaml==5.4.1",
    "requests==2.25.1",
    "typer==0.3.2",
]

install_requires += ["ignitenlp", "ontologykb"]

setup(
    name="hopeiq",
    python_requires=">=3.6",
    version=get_version("src/hopeiq"),
    author="Ian Maurer",
    author_email="ian@genomoncology.com",
    packages=find_packages("src/"),
    package_dir={"": "src"},
    package_data={
        "": ["*.lark", "*.json", "*.tsv", "*.xlsx", "*.yaml", "*.txt"]
    },
    include_package_data=True,
    entry_points={"console_scripts": ["hopeiq=hopeiq:cli"]},
    install_requires=install_requires,
    dependency_links=get_dependency_links(),
    description="",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
    ],
)
