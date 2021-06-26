from tinge import colored
from tinge.utils import InvalidColorError


def test_red():
    string = 'this is a red text'
    print(colored(string, 'red'))


def test_green():
    string = 'this is a green text'
    print(colored(string, 'green'))


def test_invalid_color():
    string = "This should raise an error"
    try:
        print(colored(string, "raise"))
    except InvalidColorError:
        print('Success')


if __name__ == "__main__":
    test_red()
    test_green()
    test_invalid_color()
