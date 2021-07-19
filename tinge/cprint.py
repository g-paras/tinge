from typing import Optional

from colorama import init  # type: ignore

from .utils import COLORS, ON_COLORS, InvalidColorError

RESET = COLORS["reset"]

init()


def colored(text: str, color: str, on_color: str = "") -> str:
    """Output colored text in terminal

    Parameter:
        text: str
        color: str
        on_color: Optional[str]

    Syntax:
        >>>colored("Hello", "red", "white")

    Available colors:
        color: ["black", "red", "green", "yellow", "blue", "magenta",
        "cyan", "white"]
        on_color: ["grey", "red", "green", "yellow", "blue", "magenta",
        "cyan", "white"]
    """
    if color in COLORS:
        color = COLORS[color]
    else:
        raise InvalidColorError(f"'{color}' is an invalid name for color")

    if on_color in ON_COLORS:
        on_color = ON_COLORS[on_color]
    else:
        raise InvalidColorError(f"'{on_color}' is an invalid name for color")

    return f"{on_color}{color}{text}{RESET}"
