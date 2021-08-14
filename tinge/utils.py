"""Utilities for cprint i.e COLORS, ONCOLORS AND Exception Class"""


class InvalidColorError(Exception):
    """Exception class for invalid colors"""


# foreground colors
COLORS = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "default": "\u001b[39m",
    "saffron": "\u001b[38;5;208m",
    "reset": "\u001b[0m",
}

# background colors
ON_COLORS = {
    "grey": "\u001b[40m",
    "red": "\u001b[41m",
    "green": "\u001b[42m",
    "yellow": "\u001b[43m",
    "blue": "\u001b[44m",
    "magenta": "\u001b[45m",
    "cyan": "\u001b[46m",
    "white": "\u001b[47m",
    "saffron": "\u001b[48;5;208m",
    "default": "\u001b[49m",
}
