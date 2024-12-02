from __future__ import annotations

from enum import auto
from typing import cast

import pytest

from stringenum import StrEnum


class Color(StrEnum):
    RED = b"red", "utf-8", "strict"
    GREEN = "green"
    BLUE = "blue"


class Planet(StrEnum):
    MERCURY = auto()
    VENUS = auto()
    EARTH = auto()


class Fruit(StrEnum):
    APPLE = "apple"
    BANANA = "banana"

    def __str__(self) -> str:
        return f"One {self.value}"


def test_color_values() -> None:
    assert cast(str, Color.RED.value) == "red"
    assert Color.GREEN.value == "green"
    assert Color.BLUE.value == "blue"


def test___str__() -> None:
    class Pet(StrEnum):
        CAT = "meow"
        DOG = "bark"

    assert str(Pet.CAT) == f"{Pet.CAT}" == "meow"
    assert str(Pet.DOG) == f"{Pet.DOG}" == "bark"


def test_color_name() -> None:
    assert Color.RED.name == "RED"
    assert Color.GREEN.name == "GREEN"
    assert Color.BLUE.name == "BLUE"


def test_color_iteration() -> None:
    colors = list(Color)
    assert len(colors) == 3
    assert colors[0] == Color.RED
    assert colors[1] == Color.GREEN
    assert colors[2] == Color.BLUE


def test_color_membership() -> None:
    assert Color.RED in Color
    assert "red" in Color
    assert "RED" not in Color
    assert "pink" not in Color
    assert None not in Color
    assert object() not in Color
    assert 1212 not in Color


def test_color_comparison() -> None:
    assert Color.RED == Color.RED
    assert Color.RED != Color.GREEN  # type: ignore[comparison-overlap]
    assert Color.RED is Color.RED
    assert Color.RED is not Color.GREEN  # type: ignore[comparison-overlap]


def test_planet_auto() -> None:
    assert Planet.MERCURY.value == "mercury"
    assert Planet.VENUS.value == "venus"
    assert Planet.EARTH.value == "earth"


def test_fruit_string_representation() -> None:
    assert str(Fruit.APPLE) == "One apple"
    assert str(Fruit.BANANA) == "One banana"


def test_strenum_exception_too_many_arguments() -> None:
    with pytest.raises(TypeError, match="too many arguments"):

        class Foo0(StrEnum):
            BAR = "bar", "utf-8", "ignore", "error"


def test_strenum_exception_not_a_string() -> None:
    with pytest.raises(TypeError, match="1 is not a string"):

        class Foo1(StrEnum):
            BAR = 1


def test_strenum_exception_encoding_must_be_string() -> None:
    with pytest.raises(TypeError, match="encoding must be a string"):

        class Foo2(StrEnum):
            BAR = "bar", object()


def test_strenum_exception_errors_must_be_string() -> None:
    with pytest.raises(TypeError, match="errors must be a string"):

        class Foo3(StrEnum):
            BAR = "bar", "utf-8", None
