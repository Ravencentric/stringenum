from __future__ import annotations

import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

if sys.version_info >= (3, 11):
    from enum import EnumType, StrEnum
else:
    from enum import Enum
    from enum import EnumMeta as EnumType

    # Copy of StrEnum for Python < 3.11
    # https://github.com/python/cpython/blob/bb98a0afd8598ce80f0e6d3f768b128eab68f40a/Lib/enum.py#L1351-L1382
    class StrEnum(str, Enum):
        """Enum where members are also (and must be) strings."""

        def __new__(cls, *values: str) -> Self:
            """Values must already be of type `str`."""
            if len(values) > 3:
                raise TypeError(f"too many arguments for str(): {values!r}")
            if len(values) == 1:
                # it must be a string
                if not isinstance(values[0], str):
                    raise TypeError(f"{values[0]!r} is not a string")
            if len(values) >= 2:
                # check that encoding argument is a string
                if not isinstance(values[1], str):
                    raise TypeError(f"encoding must be a string, not {values[1]!r}")
            if len(values) == 3:
                # check that errors argument is a string
                if not isinstance(values[2], str):
                    raise TypeError(f"errors must be a string, not {values[2]!r}")
            value = str(*values)
            member = str.__new__(cls, value)
            member._value_ = value
            return member

        @staticmethod
        def _generate_next_value_(name: str, start: int, count: int, last_values: list[str]) -> str:
            """
            Return the lower-cased version of the member name.
            """
            return name.lower()


__all__ = ("EnumType", "StrEnum")
