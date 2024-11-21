from __future__ import annotations

from typing import TYPE_CHECKING

from stringenum._compat import EnumType, StrEnum

if TYPE_CHECKING:
    from typing import TypeVar

    from typing_extensions import Self

    T = TypeVar("T", bound=EnumType)


class _CaseInsensitiveGetItem(EnumType):
    def __getitem__(self: type[T], name: str) -> T:  # type: ignore[misc]
        if not isinstance(name, str):
            raise KeyError(name)

        for key, value in self._member_map_.items():
            if key.casefold() == name.casefold():
                return value  # type: ignore[return-value]
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


class DuplicateFreeStrEnum(StrEnum):
    """
    A subclass of `StrEnum` that ensures all members have unique values and names,
    raising a `ValueError` if duplicates are found.
    """

    def __init__(self, *args: object) -> None:
        cls = self.__class__

        for member in cls:
            if self.value.casefold() == member.value.casefold():
                msg = f"Duplicate values are not allowed in {self.__class__.__name__}: {self!r}"
                raise ValueError(msg)

            if self.name.casefold() == member.name.casefold():
                msg = f"Duplicate names are not allowed in {self.__class__.__name__}: {self!r}"
                raise ValueError(msg)


class _DoubleSidedGetItemAndContains(EnumType):
    def __contains__(self: type[T], value: object) -> bool:  # type: ignore[misc]
        if isinstance(value, self):
            return True
        if isinstance(value, str):
            return value in self._value2member_map_ or any(
                value == member.name for member in self._value2member_map_.values()
            )
        return False

    def __getitem__(self: type[T], name: str) -> T:  # type: ignore[misc]
        if not isinstance(name, str):
            raise KeyError(name)

        for key, member in self._member_map_.items():
            if (key == name) or (member.value == name):
                return member  # type: ignore[return-value]
        raise KeyError(name)


class DoubleSidedStrEnum(DuplicateFreeStrEnum, metaclass=_DoubleSidedGetItemAndContains):
    """
    A subclass of `DuplicateFreeStrEnum` that supports double-sided lookup, allowing
    both member values and member names to be used for lookups.
    """

    @classmethod
    def _missing_(cls, value: object) -> Self:
        msg = f"'{value}' is not a valid {cls.__name__}"

        if isinstance(value, str):
            for member in cls:
                if (member.value == value) or (member.name == value):
                    return member
            raise ValueError(msg)
        raise ValueError(msg)


class _DoubleSidedCaseInsensitiveGetItemAndContains(EnumType):
    def __contains__(self: type[T], value: object) -> bool:  # type: ignore[misc]
        if isinstance(value, self):
            return True
        if isinstance(value, str):
            for name, member in self.__members__.items():  # type: ignore[attr-defined]
                if (value.casefold() == name.casefold()) or (member.value.casefold() == member.value.casefold()):
                    return True
        return False

    def __getitem__(self: type[T], name: str) -> T:  # type: ignore[misc]
        if not isinstance(name, str):
            raise KeyError(name)

        for key, member in self._member_map_.items():
            if (key.casefold() == name.casefold()) or (member.value.casefold() == name.casefold()):
                return member  # type: ignore[return-value]
        raise KeyError(name)


class DoubleSidedCaseInsensitiveStrEnum(DuplicateFreeStrEnum, metaclass=_DoubleSidedCaseInsensitiveGetItemAndContains):
    """
    A subclass of `DuplicateFreeStrEnum` that supports case-insenitive double-sided lookup,
    allowing both member values and member names to be used for lookups.
    """

    @classmethod
    def _missing_(cls, value: object) -> Self:
        msg = f"'{value}' is not a valid {cls.__name__}"

        if isinstance(value, str):
            for member in cls:
                if (member.value.casefold() == value.casefold()) or (member.name.casefold() == value.casefold()):
                    return member
            raise ValueError(msg)
        raise ValueError(msg)
