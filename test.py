from tinge import colored


def test_red():
    string = 'this is a red text'
    print(colored(string, 'red'))


def test_green():
    string = 'this is a green text'
    print(colored(string, 'green'))


def test_invalid_color():
    string = "This should raise an error"
    print(colored(string, "raise"))


if __name__ == "__main__":
    test_red()
    test_green()
    test_invalid_color()
