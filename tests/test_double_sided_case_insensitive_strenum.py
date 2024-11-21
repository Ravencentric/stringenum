from __future__ import annotations

import pytest

from stringenum import DoubleSidedCaseInsensitiveStrEnum


class Color(DoubleSidedCaseInsensitiveStrEnum):
    RED_COLOR = "Red"
    BLUE_SKY = "Blue"
    GREEN_GRASS = "Green"


def test_case_insensitive_getitem_by_name():
    assert Color["RED_COLOR"] is Color.RED_COLOR
    assert Color["red_color"] is Color.RED_COLOR
    assert Color["ReD_CoLoR"] is Color.RED_COLOR

    assert Color["BLUE_SKY"] is Color.BLUE_SKY
    assert Color["blue_sky"] is Color.BLUE_SKY
    assert Color["BlUe_SkY"] is Color.BLUE_SKY

    assert Color["GREEN_GRASS"] is Color.GREEN_GRASS
    assert Color["green_grass"] is Color.GREEN_GRASS
    assert Color["GreEn_GrAsS"] is Color.GREEN_GRASS


def test_case_insensitive_getitem_by_value():
    assert Color["Red"] is Color.RED_COLOR
    assert Color["red"] is Color.RED_COLOR
    assert Color["ReD"] is Color.RED_COLOR

    assert Color["Blue"] is Color.BLUE_SKY
    assert Color["blue"] is Color.BLUE_SKY
    assert Color["BlUe"] is Color.BLUE_SKY

    assert Color["Green"] is Color.GREEN_GRASS
    assert Color["green"] is Color.GREEN_GRASS
    assert Color["GreEn"] is Color.GREEN_GRASS


def test_membership():
    assert Color.RED_COLOR in Color
    assert "Red" in Color
    assert "red" in Color
    assert "GREEN_GRASS" in Color
    assert "GREEN_grass" in Color
    assert None not in Color
    assert object() not in Color
    assert 121212 not in Color


def test_case_insensitive_invalid_key():
    with pytest.raises(KeyError):
        Color["YELLOW"]

    with pytest.raises(KeyError):
        Color["yElLoW"]

    with pytest.raises(KeyError):
        Color[None]


def test_case_insensitive_lookup_by_name():
    assert Color("red_Color") is Color.RED_COLOR
    assert Color("red_color") is Color.RED_COLOR
    assert Color("blue_SKY") is Color.BLUE_SKY
    assert Color("BLUE_SKY") is Color.BLUE_SKY
    assert Color("grEEn_GRASS") is Color.GREEN_GRASS
    assert Color("green_grass") is Color.GREEN_GRASS


def test_case_insensitive_lookup_by_value():
    assert Color("red") is Color.RED_COLOR
    assert Color("RED") is Color.RED_COLOR
    assert Color("blue") is Color.BLUE_SKY
    assert Color("BLUE") is Color.BLUE_SKY
    assert Color("green") is Color.GREEN_GRASS
    assert Color("GREEN") is Color.GREEN_GRASS


def test_value_error_on_invalid_lookup():
    with pytest.raises(ValueError):
        Color("YELLOW")

    with pytest.raises(ValueError):
        Color("yellow")

    with pytest.raises(ValueError):
        Color(None)


def test_unique_values():
    with pytest.raises(ValueError):

        class InvalidColor(DoubleSidedCaseInsensitiveStrEnum):
            RED_COLOR = "Red"
            BLUE_SKY = "Blue"
            BLUE_DUPLICATE = "Blue"


def test_unique_values_case_insensitively():
    with pytest.raises(ValueError):

        class InvalidColor(DoubleSidedCaseInsensitiveStrEnum):
            RED_COLOR = "Red"
            BLUE_SKY = "Blue"
            BLUE_DUPLICATE = "blue"


def test_unique_names():
    with pytest.raises(TypeError):

        class InvalidColor(DoubleSidedCaseInsensitiveStrEnum):
            RED = "Red"
            BLUE = "Blue"
            BLUE = "Green"


def test_unique_names_case_insensitively():
    with pytest.raises(ValueError):

        class InvalidColor(DoubleSidedCaseInsensitiveStrEnum):
            RED = "Red"
            BLUE = "Blue"
            blue = "Green"
