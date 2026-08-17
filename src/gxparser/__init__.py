"""GXParser public API."""

from .gx import read_file as read_gx
from .xfi import read_file as read_xfi
from .xfi import read_for_gx

__all__ = ["read_gx", "read_xfi", "read_for_gx"]
__version__ = "0.7.0b1"
