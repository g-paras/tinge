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


def bold(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored bold text

    Parameter:
        text: str

    Syntax:
        >>> print(bold(text), color[Optional], color[Optional])
    """

    return colored(f"\u001b[1m{text}{RESET}", color, on_color)


def italic(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored italic text

    Parameter:
        text: str

    Syntax:
        >>> print(italic(text, color[Optional], on_color[Optional]))
    """

    return colored(f"\u001b[3m{text}{RESET}", color, on_color)


def underline(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored underline text

    Parameter:
        text: str

    Syntax:
        >>> print(underline(text), color[Optional], on_color[Optional])
    """

    return colored(f"\u001b[4m{text}{RESET}", color, on_color)


def warn(text: str, strong: bool = True) -> str:
    """Output warning with yellow text

    Parameter:
        text: str

    Syntax:
        >>> print(warn(text))
    """
    if strong:
        return bold(text, "yellow")
    return colored(text, "yellow")


def error(text: str, strong: bool = True) -> str:
    """Output error with red text

    Parameter:
        text: str

    Syntax:
        >>> print(error(text))
    """
    if strong:
        return bold(text, "red")
    return colored(text, "red")


def info(text: str, strong: bool = True) -> str:
    """Output info with blue text

    Parameter:
        text: str

    Syntax:
        >>> print(info(text))
    """
    if strong:
        return bold(text, "blue")
    return colored(text, "blue")


def success(text: str, strong: bool = True) -> str:
    """Output success with green text

    Parameter:
        text: str

    Syntax:
        >>> print(success(text))
    """
    if strong:
        return bold(text, "green")
    return colored(text, "green")
