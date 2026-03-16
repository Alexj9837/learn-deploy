"""FastAPI application for first_step."""

from fastapi import FastAPI

from . import __version__, pi

app = FastAPI(title="first-step", version=__version__)


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    """Liveness probe endpoint."""
    return {"status": "ok"}


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"service": "first-step", "version": __version__}


@app.get("/pi/all/{n}")
async def find_all_in_pi(n: int) -> dict[str, int | list[int]]:
    return {"n": n, "positions": pi.find_all_pos_in_pi(n)}


@app.get("/pi/{n}")
async def find_in_pi(n: int) -> dict[str, int | None]:
    return {"n": n, "position": pi.find__first_in_pi(n)}
