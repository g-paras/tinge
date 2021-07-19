import pathlib
import platform
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

INSTALL_REQUIRES = []

if platform.system() == "Windows":
    INSTALL_REQUIRES.append("colorama")

setup(
    name="Tinge",
    version="0.0.2",
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
    install_requires=INSTALL_REQUIRES,
)
