import fixpath
from tinge import colored, InvalidColorError


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
        print('Success: InvalidColorError occurred and handles')


def test_red_on_white():
    string = "This is red on white"
    print(colored(string, "red", "white"))


if __name__ == "__main__":
    test_red()
    test_green()
    test_invalid_color()
    test_red_on_white()
