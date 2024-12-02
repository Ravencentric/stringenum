from __future__ import annotations

import nox

nox.needs_version = ">=2024.10.9"
nox.options.default_venv_backend = "uv|virtualenv"


def dev_group() -> list[str]:
    return nox.project.load_toml("pyproject.toml")["dependency-groups"]["dev"]  # type: ignore[no-any-return]


@nox.session
def lint(session: nox.Session) -> None:
    session.install(".", *dev_group(), silent=True)
    session.run("ruff", "check", ".", "--fix")
    session.run("ruff", "format", ".")
    session.run("mypy", ".")


@nox.session(python=["3.9", "3.10", "3.11", "3.12", "3.13"])
def test(session: nox.Session) -> None:
    session.install(".", *dev_group(), silent=True)
    session.run("coverage", "run", "-m", "pytest", "-vv", *session.posargs)


@nox.session
def coverage(session: nox.Session) -> None:
    session.install(".", *dev_group(), silent=True)
    session.run("coverage", "combine")
    session.run("coverage", "report", "-m")
    session.run("coverage", "xml")
