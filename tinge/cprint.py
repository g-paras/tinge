from typing import Optional

from .utils import InvalidColorError, COLORS, ON_COLORS

RESET = COLORS["reset"]


def colored(text: str, color: str, on_color: Optional[str] = '') -> str:
    if color in COLORS:
        color = COLORS[color]
    else:
        raise InvalidColorError(f"'{color}' is an invalid name for color")

    if on_color in ON_COLORS:
        on_color = ON_COLORS[on_color]
    else:
        raise InvalidColorError(f"'{on_color}' is an invalid name for color")

    return f"{on_color}{color}{text}{RESET}"
