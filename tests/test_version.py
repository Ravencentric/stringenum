from __future__ import annotations

import tomli

from stringenum import __version__


def test_versions_match() -> None:
    pyproject_version: str = tomli.load(open("pyproject.toml", "rb"))["project"]["version"]
    assert pyproject_version == __version__
