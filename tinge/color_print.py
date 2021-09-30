"""Implementation of all functions"""

import platform
from os import get_terminal_size, system

from .utils import COLORS, ON_COLORS, InvalidColorError

RESET = COLORS["reset"]

if platform.system() == "Windows":
    system("")


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


def cprint(text: str, color: str, on_color: str = "default") -> None:
    """Print colored text

    Parameter:
        text: str
        color: str
        on_color: Optional[str]

    Syntax:
        >>>cprint("Hello", "red", "white")

    Available colors:
        color: ["black", "red", "green", "yellow", "blue", "magenta",
        "cyan", "white"]
        on_color: ["grey", "red", "green", "yellow", "blue", "magenta",
        "cyan", "white"]
    """
    print(colored(text, color, on_color))


def bold(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored bold text

    Parameter:
        text: str
        color: Optional[str]
        on_color: Optional[str]

    Syntax:
        >>> print(bold(text, color[Optional], color[Optional]))
    """
    return colored(f"\u001b[1m{text}{RESET}", color, on_color)


def italic(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored italic text

    Parameter:
        text: str
        color: Optional[str]
        on_color: Optional[str]

    Syntax:
        >>> print(italic(text, color[Optional], on_color[Optional]))
    """
    return colored(f"\u001b[3m{text}{RESET}", color, on_color)


def underline(text: str, color: str = "default", on_color: str = "default") -> str:
    """Output colored underline text

    Parameter:
        text: str
        color: Optional[str]
        on_color: Optional[str]

    Syntax:
        >>> print(underline(text, color[Optional], on_color[Optional]))
    """
    return colored(f"\u001b[4m{text}{RESET}", color, on_color)


def warn(text: str, strong: bool = True) -> None:
    """Output warning with yellow text

    Parameter:
        text: str
        strong: Optional[bool]

    Syntax:
        >>> warn(text)
    """
    if strong:
        print(bold(text, "yellow"))
        return
    print(colored(text, "yellow"))
    return


def error(text: str, strong: bool = True) -> None:
    """Output error with red text

    Parameter:
        text: str
        strong: Optional[bool]

    Syntax:
        >>> error(text)
    """
    if strong:
        print(bold(text, "red"))
        return
    print(colored(text, "red"))
    return


def info(text: str, strong: bool = True) -> None:
    """Output info with blue text

    Parameter:
        text: str
        strong: Optional[bool]

    Syntax:
        >>> info(text)
    """
    if strong:
        print(bold(text, "blue"))
        return
    print(colored(text, "blue"))
    return


def success(text: str, strong: bool = True) -> None:
    """Output success with green text

    Parameter:
        text: str
        strong: Optional[bool]

    Syntax:
        >>> success(text)
    """
    if strong:
        print(bold(text, "green"))
        return
    print(colored(text, "green"))
    return


def red(text: str, on_color: str = "default"):
    """output formatted red text

    Parameter:
        text: str
        on_color: Optonal[str]

    Syntax:
        >>> red(text)
    """
    return colored(text, "red", on_color=on_color)


def white(text: str, on_color: str = "default"):
    """output formatted white text

    Parameter:
        text: str
        on_color: Optonal[str]

    Syntax:
        >>> white(text)
    """
    return colored(text, "white", on_color)


def black(text: str, on_color: str = "default"):
    """output formatted black text

    Parameter:
        text: str
        on_color: Optonal[str]

    Syntax:
        >>> black(text)
    """
    return colored(text, "black", on_color)


def blue(text: str, on_color: str = "default"):
    """output formatted blue text

    Parameter:
        text: str
        on_color: Optonal[str]

    Syntax:
        >>> blue(text)
    """
    return colored(text, "blue", on_color)


def green(text: str, on_color: str = "default"):
    """output formatted green text

    Parameter:
        text: str
        on_color: Optonal[str]

    Syntax:
        >>> green(text)
    """
    return colored(text, "green", on_color)


def yellow(text: str, on_color: str = "default"):
    """output formatted yellow text

    Parameter:
        text: str
        on_color: Optonal[str]

    Syntax:
        >>> yellow(text)
    """
    return colored(text, "yellow", on_color)


def cyan(text: str, on_color: str = "default"):
    """output formatted cyan text

    Parameter:
        text: str
        on_color: Optonal[str]

    Syntax:
        >>> cyan(text)
    """
    return colored(text, "cyan", on_color)


def line(
    text: str = "",
    sep: str = "-",
    color: str = "default",
    on_color: str = "default",
) -> None:
    """Print horizontal line with length equal to width of terminal

    Parameter:
        text: Optional[str]
        sep: Optional[str]
        color: Optional[str]
        on_color: Optional[str]

    Syntax:
        >>> line("Hello", color="red")
    """
    # get_terminal_size function raise OSError in Jupyter Notebooks
    try:
        width, _ = get_terminal_size()
    except OSError:
        # set width to 80 according to black
        width = 80
    cprint((f" {text} " if text else "").center(width - 1, sep), color, on_color)
