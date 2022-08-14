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
        bold("76th Independence", "white"),
        bold("Day", "green"),
    )

    print("\n")


def banner():
    try:
        length, _ = get_terminal_size()
    except OSError:
        length = 80

    sleep_time = 0.1

    main_text = "Thank You for using Tinge, made with ❤  by Paras Gupta"
    text = main_text + " "*max(0, length-len(main_text))

    for i in range(1, length+1):
        print(f"\r{text[:i].rjust(length, ' ')}", end="")
        sleep(sleep_time)

    for i in range(1, len(main_text)+1):
        print(f"\r{text[i:].ljust(length, ' ')}"[:length+1], end="")
        sleep(sleep_time)

    print("Please leave a ⭐ on github".center(length-1, " "))
    print("(github.com/g-paras/tinge)".center(length-1, " "))
    print("\n\n")

flag()
banner()