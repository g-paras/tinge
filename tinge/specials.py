from os import get_terminal_size
from . import colored, bold


def flag():
    """Independence Day Special"""
    try:
        length, _ = get_terminal_size()
    except:
        length = 80

    print("\n\n")
    print(colored("                ", "saffron", "saffron").center(length + 25, " "))
    print(colored("       \u2699        ", "saffron", "white").center(length + 19, " "))
    print(colored("                ", "saffron", "green").center(length + 19, " "))

    print()
    print(
        " " * ((length - 26) // 2),
        bold("Happy", "saffron"),
        "75th",
        bold("Independence", "white"),
        bold("Day", "green"),
    )

    print("\n\n")
    print("Made with ❤ by Paras".center(length, " "))


flag()
