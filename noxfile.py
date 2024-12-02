from __future__ import annotations

import nox

nox.needs_version = ">=2024.10.9"
nox.options.default_venv_backend = "uv"


def install(session: nox.Session) -> None:
    """Install the current project."""
    session.run_install(
        "uv",
        "sync",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
        silent=True,
    )


@nox.session
def lint(session: nox.Session) -> None:
    """Run ruff and mypy."""
    install(session)
    session.run("ruff", "check", ".", "--fix")
    session.run("ruff", "format", ".")
    session.run("mypy", ".")


@nox.session(python=["3.9", "3.10", "3.11", "3.12", "3.13"])
def test(session: nox.Session) -> None:
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
