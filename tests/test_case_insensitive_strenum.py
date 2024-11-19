from __future__ import annotations

import pytest

from stringenum import CaseInsensitiveStrEnum


class Color(CaseInsensitiveStrEnum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"


def test_case_insensitive_getitem():
    assert Color["red"] is Color.RED
    assert Color["RED"] is Color.RED
    assert Color["ReD"] is Color.RED
    assert Color["blue"] is Color.BLUE
    assert Color["BLUE"] is Color.BLUE
    assert Color["Green"] is Color.GREEN


def test_case_insensitive_missing():
    assert Color("red") is Color.RED
    assert Color("RED") is Color.RED
    assert Color("BlUe") is Color.BLUE
    assert Color("green") is Color.GREEN


def test_invalid_enum_value():
    with pytest.raises(ValueError):
        Color("invalid_color")

    with pytest.raises(ValueError):
        Color(None)


def test_invalid_enum_key():
    with pytest.raises(KeyError):
        Color["nonexistent_color"]

    with pytest.raises(KeyError):
        Color[None]
