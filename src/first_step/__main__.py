"""Interface for ``python -m first_step``."""

from argparse import ArgumentParser
from collections.abc import Sequence

import uvicorn

from . import __version__

__all__ = ["main"]


def main(args: Sequence[str] | None = None) -> None:
    """Argument parser for the CLI."""
    parser = ArgumentParser(description="first-step service")
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=__version__,
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",  # noqa: S104
        help="Host to bind (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to listen on (default: 8000)",
    )
    parsed = parser.parse_args(args)
    uvicorn.run(
        "first_step.app:app",
        host=parsed.host,
        port=parsed.port,
    )


if __name__ == "__main__":
    main()
