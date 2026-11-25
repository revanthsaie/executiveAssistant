"""Local HTTP API. Serves JSON under /api and the built React UI at /."""

import platform

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from executive_assistant import __version__
from executive_assistant.paths import frontend_dir


def create_app() -> FastAPI:
    """Build the FastAPI app.

    API routes are registered before the static mount, because a mount at "/"
    would otherwise swallow every request, including /api/*.
    """
    app = FastAPI(title="Executive Assistant", version=__version__)

    @app.get("/api/health")
    def health() -> dict:
        """Report that the backend is alive, plus basic runtime info for M0 checks."""
        return {
            "status": "ok",
            "version": __version__,
            "python": platform.python_version(),
            "os": f"{platform.system()} {platform.release()}",
        }

    ui_dir = frontend_dir()
    if ui_dir.is_dir():
        app.mount("/", StaticFiles(directory=ui_dir, html=True), name="ui")

    return app
