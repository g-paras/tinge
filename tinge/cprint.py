from typing import Optional

from .utils import InvalidColorError, color_pair

RESET = color_pair["reset"]


def colored(text: str, color: str, on: Optional[str] = '') -> str:
    if color in color_pair:
        color = color_pair[color]
    else:
        raise InvalidColorError(f"'{color}' is an invalid name for color")

    return f"{color}{text}{RESET}"
