import fixpath # to insert tinge module in path

from tinge import InvalidColorError, colored, italic, underline
import pytest


def test_red():
    """check red color is working or not"""
    string = "this is a red text"
    print(colored(string, "red"))


def test_green():
    string = "this is a green text"
    print(colored(string, "green"))


def test_invalid_color():
    string = "This should raise an error"
    with pytest.raises(InvalidColorError):
        print(colored(string, "raise"))  # invalid color name


def test_red_on_white():
    string = "This is red on white"
    print(colored(string, "red", "white"))


def test_italic():
    string = "some random  string"
    print(italic(string))


def test_underline():
    string = "another random string"
    print(underline(string))


if __name__ == "__main__":
    test_red()
    test_green()
    test_invalid_color()
    test_red_on_white()
