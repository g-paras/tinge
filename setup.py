import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


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
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["tinge"],
    install_requires=["colorama"],
)
