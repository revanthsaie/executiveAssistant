"""Locate bundled resources both in development and inside a PyInstaller build."""

import sys
from pathlib import Path


def resource_root() -> Path:
    """Return the folder that holds bundled resources.

    PyInstaller unpacks bundled files into a folder exposed as ``sys._MEIPASS``.
    In development there is no such attribute, so we fall back to the repo root
    (two levels up from this file: src/executive_assistant/ -> repo).
    """
    bundle_dir = getattr(sys, "_MEIPASS", None)
    if bundle_dir:
        return Path(bundle_dir)
    return Path(__file__).resolve().parents[2]


def frontend_dir() -> Path:
    """Return the folder with the built React app (index.html + assets)."""
    return resource_root() / "frontend" / "build"
