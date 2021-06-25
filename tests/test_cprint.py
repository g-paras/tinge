from tinge import colored


def test_red():
    string = 'my name is paras'
    print(colored(string, 'red'))


def test_green():
    string = 'this is a green text'
    print(colored(string, 'green'))


if __name__ == "__main__":
    test_red()
