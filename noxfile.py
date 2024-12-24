from __future__ import annotations

import os

import nox

nox.needs_version = ">=2024.10.9"
nox.options.default_venv_backend = "uv"

PYTHON_VERSIONS = ("3.9", "3.10", "3.11", "3.12", "3.13")


def install(session: nox.Session) -> None:
    """Install the current project."""
    session.run_install(
        "uv",
        "sync",
        "--locked",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
        silent=True,
    )


@nox.session
def ruff(session: nox.Session) -> None:
    """Run ruff."""
    install(session)

    if os.getenv("CI"):
        # Do not modify files in CI, simply fail.
        session.run("ruff", "check", ".")
        session.run("ruff", "format", ".", "--check")
    else:
        # Fix any fixable errors if running locally.
        session.run("ruff", "check", ".", "--fix")
        session.run("ruff", "format", ".")


@nox.session(python=PYTHON_VERSIONS)
def mypy(session: nox.Session) -> None:
    """Run mypy."""
    install(session)
    session.run("mypy")


@nox.session(python=PYTHON_VERSIONS)
def pytest(session: nox.Session) -> None:
    """Run tests."""
    install(session)
    datafile = f".coverage.{session.python}"
    session.run("coverage", "run", f"--data-file={datafile}", "-m", "pytest", "-vv", *session.posargs)


@nox.session
def coverage(session: nox.Session) -> None:
    """Generate and report coverage."""
    install(session)
    session.run("coverage", "combine")
    session.run("coverage", "report", "-m")
    session.run("coverage", "xml")
