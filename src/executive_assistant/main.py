"""Desktop entry point: start the local API in a background thread, then open a window.

Flow:
    pick a free port on 127.0.0.1 -> run uvicorn in a daemon thread
    -> wait until /api/health answers -> open the pywebview window on it.
Closing the window ends the process; the daemon thread dies with it.
"""

import os
import socket
import sys
import threading
import time
import urllib.request

import uvicorn
import webview

from executive_assistant.api import create_app

HOST = "127.0.0.1"  # local only: nothing else on the network can reach the API


def find_free_port() -> int:
    """Ask the OS for an unused TCP port, so two copies never clash on a fixed port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, 0))
        return sock.getsockname()[1]


def start_server(port: int) -> None:
    """Run uvicorn in a daemon thread so it stops when the window closes."""
    config = uvicorn.Config(create_app(), host=HOST, port=port, log_level="warning")
    server = uvicorn.Server(config)
    threading.Thread(target=server.run, daemon=True).start()


def wait_until_ready(url: str, timeout_s: float = 15.0) -> None:
    """Poll the health endpoint until the server answers, or raise after the timeout."""
    deadline = time.monotonic() + timeout_s
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=1) as resp:
                if resp.status == 200:
                    return
        except OSError:
            time.sleep(0.1)
    raise RuntimeError(f"Backend did not start within {timeout_s}s: {url}")


def ensure_std_streams() -> None:
    """Give the process real stdout/stderr when built without a console.

    A windowed PyInstaller build (no console) sets sys.stdout/stderr to None, and
    uvicorn's logging crashes when it writes to them. Point them at devnull instead.
    """
    if sys.stdout is None:
        sys.stdout = open(os.devnull, "w")
    if sys.stderr is None:
        sys.stderr = open(os.devnull, "w")


def main() -> None:
    """Start the backend and open the app window."""
    ensure_std_streams()
    # EA_PORT pins the port so `npm run dev` can proxy to it; otherwise pick any free one.
    port = int(os.environ.get("EA_PORT") or find_free_port())
    base_url = f"http://{HOST}:{port}"
    start_server(port)
    wait_until_ready(f"{base_url}/api/health")
    webview.create_window("Executive Assistant", base_url, width=1200, height=800, min_size=(900, 600))
    webview.start()


if __name__ == "__main__":
    main()
