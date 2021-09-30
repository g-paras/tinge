"""Entry point for import"""

from .color_print import (
    bold,
    colored,
    cprint,
    error,
    hline,
    info,
    italic,
    success,
    underline,
    warn,
)
from .utils import InvalidColorError

__version__ = "0.0.6"
__all__ = [
    "bold",
    "colored",
    "cprint",
    "error",
    "hline",
    "info",
    "italic",
    "success",
    "underline",
    "warn",
    "InvalidColorError",
]
