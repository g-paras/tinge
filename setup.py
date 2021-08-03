# stdlib imports
import pathlib

# external imports
from setuptools import setup

# local imports
from tinge import __version__

VERSION = __version__

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="Tinge",
    version=VERSION,
    description="Colored text for terminal",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/g-paras/tinge",
    author="Paras Gupta",
    author_email="guptaparas039@gmail.com",
    license="MIT",
    python_requires=">=3.5",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Topic :: Terminals",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    packages=["tinge"],
)
