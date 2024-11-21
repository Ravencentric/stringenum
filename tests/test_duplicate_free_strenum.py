from __future__ import annotations

import pytest

from stringenum import DuplicateFreeStrEnum


def test_duplicate_value_raises_error():
    with pytest.raises(ValueError, match="Duplicate values are not allowed in Color"):

        class ColorWithDuplicateValue(DuplicateFreeStrEnum):
            RED = "red"
            GREEN = "green"
            BLUE = "Red"  # This should raise an error because "Red" == "red" (case-insensitive)


def test_duplicate_name_raises_error():
    with pytest.raises(ValueError, match="Duplicate names are not allowed in Color"):

        class ColorWithDuplicateName(DuplicateFreeStrEnum):
            RED = "red"
            GREEN = "green"
            Red = "Blue"
