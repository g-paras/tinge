"""Entry point for import"""

from .color_print import (
    bold,
    colored,
    cprint,
    error,
    line,
    info,
    italic,
    success,
    underline,
    warn,
    red,
    green,
    blue,
    cyan,
    white,
    black,
    yellow,
)
from .utils import InvalidColorError

__version__ = "0.0.7"
__all__ = [
    "red",
    "green",
    "blue",
    "cyan",
    "white",
    "black",
    "yellow",
    "bold",
    "colored",
    "cprint",
    "error",
    "line",
    "info",
    "italic",
    "success",
    "underline",
    "warn",
    "InvalidColorError",
]
