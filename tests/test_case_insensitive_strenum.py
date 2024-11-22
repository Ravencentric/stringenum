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


def test_membership():
    class Pet(CaseInsensitiveStrEnum):
        CAT = "meow"
        DOG = "bark"

    assert Pet.CAT in Pet
    assert "CAT" not in Pet
    assert "MEow" in Pet
    assert "dog" not in Pet
    assert "BARK" in Pet
    assert None not in Pet
    assert object() not in Pet
    assert 121212 not in Pet


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


def test_unique_on_each_side():
    class ValidColor(CaseInsensitiveStrEnum):
        RED_COLOR = "RED_COLOR"
        BLUE_SKY = "BLUE_SKY"

    assert ValidColor.RED_COLOR is ValidColor.RED_COLOR


def test_unique_values_case_insensitively():
    with pytest.raises(ValueError):

        class InvalidColor(CaseInsensitiveStrEnum):
            RED_COLOR = "Red"
            BLUE_SKY = "Blue"
            BLUE_DUPLICATE = "blue"


def test_unique_names():
    with pytest.raises(TypeError):

        class InvalidColor(CaseInsensitiveStrEnum):
            RED = "Red"
            BLUE = "Blue"
            BLUE = "Green"


def test_unique_names_case_insensitively():
    with pytest.raises(ValueError):

        class InvalidColor(CaseInsensitiveStrEnum):
            RED = "Red"
            BLUE = "Blue"
            blue = "Green"
