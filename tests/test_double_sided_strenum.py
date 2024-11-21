from __future__ import annotations

import pytest

from stringenum import DoubleSidedStrEnum


class Color(DoubleSidedStrEnum):
    RED_COLOR = "Red"
    BLUE_SKY = "Blue"
    GREEN_GRASS = "Green"


def test_getitem_by_name():
    assert Color["RED_COLOR"] is Color.RED_COLOR
    assert Color["BLUE_SKY"] is Color.BLUE_SKY
    assert Color["GREEN_GRASS"] is Color.GREEN_GRASS


def test_getitem_by_value():
    assert Color["Red"] is Color.RED_COLOR
    assert Color["Blue"] is Color.BLUE_SKY
    assert Color["Green"] is Color.GREEN_GRASS


def test_membership():
    assert Color.RED_COLOR in Color
    assert "Red" in Color
    assert "red" not in Color
    assert "GREEN_GRASS" in Color
    assert "GREEN_grass" not in Color
    assert None not in Color
    assert object() not in Color
    assert 121212 not in Color


def test_getitem_invalid_key():
    with pytest.raises(KeyError):
        Color["YELLOW"]

    with pytest.raises(KeyError):
        Color["Red_color"]

    with pytest.raises(KeyError):
        Color[None]


def test_lookup_by_name():
    assert Color("RED_COLOR") is Color.RED_COLOR
    assert Color("BLUE_SKY") is Color.BLUE_SKY
    assert Color("BLUE_SKY") is Color.BLUE_SKY


def test_lookup_by_value():
    assert Color("Red") is Color.RED_COLOR
    assert Color("Blue") is Color.BLUE_SKY
    assert Color("Green") is Color.GREEN_GRASS


def test_value_error_on_invalid_lookup():
    with pytest.raises(ValueError):
        Color("YELLOW")

    with pytest.raises(ValueError):
        Color("Red_color")

    with pytest.raises(ValueError):
        Color(None)


def test_unique_values():
    with pytest.raises(ValueError):

        class InvalidColor(DoubleSidedStrEnum):
            RED_COLOR = "Red"
            BLUE_SKY = "Blue"
            BLUE_DUPLICATE = "Blue"


def test_unique_values_case_insensitively():
    with pytest.raises(ValueError):

        class InvalidColor(DoubleSidedStrEnum):
            RED_COLOR = "Red"
            BLUE_SKY = "Blue"
            BLUE_DUPLICATE = "blue"


def test_unique_names():
    with pytest.raises(TypeError):

        class InvalidColor(DoubleSidedStrEnum):
            RED = "Red"
            BLUE = "Blue"
            BLUE = "Green"


def test_unique_names_case_insensitively():
    with pytest.raises(ValueError):

        class InvalidColor(DoubleSidedStrEnum):
            RED = "Red"
            BLUE = "Blue"
            blue = "Green"
