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
    class StrEnum(str, Enum):  # pragma: no cover
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


__version__ = "0.1.0"

__all__ = (
    "StrEnum",
    "CaseInsensitiveStrEnum",
    "DoubleSidedStrEnum",
    "DoubleSidedCaseInsensitiveStrEnum",
    "__version__",
)


class _CaseInsensitiveGetItem(EnumType):
    def __getitem__(cls, name: str) -> Self:  # type: ignore[explicit-override, misc, override]
        if not isinstance(name, str):
            raise KeyError(name)

        for key, value in super().__dict__["_member_map_"].items():
            if key.casefold() == name.casefold():
                return value  # type: ignore[no-any-return]
        raise KeyError(name)


class CaseInsensitiveStrEnum(StrEnum, metaclass=_CaseInsensitiveGetItem):
    """A subclass of `StrEnum` that supports case-insensitive lookup."""

    @classmethod
    def _missing_(cls, value: object) -> Self:
        msg = f"'{value}' is not a valid {cls.__name__}"

        if isinstance(value, str):
            for member in cls:
                if member.value.casefold() == value.casefold():
                    return member
            raise ValueError(msg)
        raise ValueError(msg)


class _DoubleSidedGetItem(EnumType):
    def __getitem__(cls, name: str) -> Self:  # type: ignore[explicit-override, misc, override]
        if not isinstance(name, str):
            raise KeyError(name)

        for key, member in super().__dict__["_member_map_"].items():
            if (key == name) or (member.value == name):
                return member  # type: ignore[no-any-return]
        raise KeyError(name)


class DoubleSidedStrEnum(StrEnum, metaclass=_DoubleSidedGetItem):
    """
    A subclass of `StrEnum` that supports double-sided lookup, allowing
    both member values and member names to be used for lookups.
    It also ensures that each member has a unique value.
    """

    def __init__(self, *args: object) -> None:
        cls = self.__class__
        if any(self.value == member.value for member in cls):
            a = self.name
            e = cls(self.value).name
            msg = f"Aliases not allowed in {self.__class__.__name__}:  {a!r} --> {e!r}"
            raise ValueError(msg)

    @classmethod
    def _missing_(cls, value: object) -> Self:
        msg = f"'{value}' is not a valid {cls.__name__}"

        if isinstance(value, str):
            for member in cls:
                if (member.value == value) or (member.name == value):
                    return member
            raise ValueError(msg)
        raise ValueError(msg)


class _DoubleSidedCaseInsensitiveGetItem(EnumType):
    def __getitem__(cls, name: str) -> Self:  # type: ignore[explicit-override, misc, override]
        if not isinstance(name, str):
            raise KeyError(name)

        for key, member in super().__dict__["_member_map_"].items():
            if (key.casefold() == name.casefold()) or (member.value.casefold() == name.casefold()):
                return member  # type: ignore[no-any-return]
        raise KeyError(name)


class DoubleSidedCaseInsensitiveStrEnum(StrEnum, metaclass=_DoubleSidedCaseInsensitiveGetItem):
    """
    A subclass of `StrEnum` that supports case-insenitive double-sided lookup,
    allowing both member values and member names to be used for lookups.
    It also ensures that each member has a unique value.
    """

    def __init__(self, *args: object) -> None:
        cls = self.__class__
        if any(self.value == member.value for member in cls):
            a = self.name
            e = cls(self.value).name
            msg = f"Aliases not allowed in {self.__class__.__name__}:  {a!r} --> {e!r}"
            raise ValueError(msg)

    @classmethod
    def _missing_(cls, value: object) -> Self:
        msg = f"'{value}' is not a valid {cls.__name__}"

        if isinstance(value, str):
            for member in cls:
                if (member.value.casefold() == value.casefold()) or (member.name.casefold() == value.casefold()):
                    return member
            raise ValueError(msg)
        raise ValueError(msg)
