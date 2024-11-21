from __future__ import annotations

from enum import auto

import pytest

from stringenum import StrEnum


class Color(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Planet(StrEnum):
    MERCURY = auto()
    VENUS = auto()
    EARTH = auto()


class Fruit(StrEnum):
    APPLE = "apple"
    BANANA = "banana"

    def __str__(self):
        return f"One {self.value}"


def test_color_values():
    assert Color.RED.value == "red"
    assert Color.GREEN.value == "green"
    assert Color.BLUE.value == "blue"


def test___str__():
    class Pet(StrEnum):
        CAT = "meow"
        DOG = "bark"

    assert str(Pet.CAT) == f"{Pet.CAT}" == "meow"
    assert str(Pet.DOG) == f"{Pet.DOG}" == "bark"


def test_color_name():
    assert Color.RED.name == "RED"
    assert Color.GREEN.name == "GREEN"
    assert Color.BLUE.name == "BLUE"


def test_color_iteration():
    colors = list(Color)
    assert len(colors) == 3
    assert colors[0] == Color.RED
    assert colors[1] == Color.GREEN
    assert colors[2] == Color.BLUE


def test_color_membership():
    assert Color.RED in Color
    assert "red" in Color
    assert "RED" not in Color
    assert "pink" not in Color
    assert None not in Color
    assert object() not in Color
    assert 1212 not in Color


def test_color_comparison():
    assert Color.RED == Color.RED
    assert Color.RED != Color.GREEN
    assert Color.RED is Color.RED
    assert Color.RED is not Color.GREEN


def test_planet_auto():
    assert Planet.MERCURY.value == "mercury"
    assert Planet.VENUS.value == "venus"
    assert Planet.EARTH.value == "earth"


def test_fruit_string_representation():
    assert str(Fruit.APPLE) == "One apple"
    assert str(Fruit.BANANA) == "One banana"


def test_strenum_exceptions():
    with pytest.raises(TypeError, match="too many arguments"):

        class Foo(StrEnum):
            BAR = "bar", "utf-8", "ignore", "error"

    with pytest.raises(TypeError, match="1 is not a string"):

        class Foo(StrEnum):
            BAR = 1

    with pytest.raises(TypeError, match="encoding must be a string"):

        class Foo(StrEnum):
            BAR = "bar", object()

    with pytest.raises(TypeError, match="errors must be a string"):

        class Foo(StrEnum):
            BAR = "bar", "utf-8", None
