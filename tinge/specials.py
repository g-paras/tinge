from os import get_terminal_size
from time import sleep

from . import colored, bold


def flag():
    """Independence Day Special"""
    try:
        length, _ = get_terminal_size()
    except OSError:
        length = 80

    print("\n\n")
    print(colored(" " * 16, "saffron", "saffron").center(length + 25, " "))
    print(colored("       \u2699        ", "saffron", "white").center(length + 19, " "))
    print(colored(" " * 16, "saffron", "green").center(length + 19, " "))

    print()
    print(
        " " * ((length - 26) // 2),
        bold("Happy", "saffron"),
        bold("75th Independence", "white"),
        bold("Day", "green"),
    )

    print("\n\n")
    print("Made with ❤ by Paras".center(length, " "))


flag()


def banner():
    text = "Thank You for using Tinge, made with ❤ in India"

    try:
        length, _ = get_terminal_size()
    except OSError:
        length = 80

    for i in range(1, length):
        print(f"\r{text[:i].rjust(length, ' ')}", end="")
        sleep(0.1)

