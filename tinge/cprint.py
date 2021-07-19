import platform

from .utils import COLORS, ON_COLORS, InvalidColorError

RESET = COLORS["reset"]

if platform.system() == "Windows":
    from colorama import init  # type: ignore

    init()


def colored(text: str, color: str, on_color: str = "default") -> str:
    """Output colored text in terminal

    Parameter:
        text: str
        color: str
        on_color: Optional[str]

    Syntax:
        >>>print(colored("Hello", "red", "white"))

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


def warn(text: str):
    """Output warning with yellow text

    Parameter:
        text: str

    Syntax:
        >>> print(warn(text))
    """

    return colored(text, "yellow")


def error(text: str):
    """Output error with red text

    Parameter:
        text: str

    Syntax:
        >>> print(error(text))
    """

    return colored(text, "red")


def info(text: str):
    """Output info with blue text

    Parameter:
        text: str

    Syntax:
        >>> print(info(text))
    """

    return colored(text, "blue")


def success(text: str):
    """Output success with green text

    Parameter:
        text: str

    Syntax:
        >>> print(success(text))
    """

    return colored(text, "green")


def bold(text: str):
    """Output bold text

    Parameter:
        text: str

    Syntax:
        >>> print(bold(text))
    """

    return f"\u001b[1m{text}{RESET}"


def italic(text: str):
    """Output italic text

    Parameter:
        text: str

    Syntax:
        >>> print(italic(text))
    """

    return f"\u001b[3m{text}{RESET}"


def underline(text: str):
    """Output underline text

    Parameter:
        text: str

    Syntax:
        >>> print(underline(text))
    """

    return f"\u001b[4m{text}{RESET}"
