from __future__ import annotations

from stringenum._compat import StrEnum
from stringenum._core import (
    CaseInsensitiveStrEnum,
    DoubleSidedCaseInsensitiveStrEnum,
    DoubleSidedStrEnum,
    DuplicateFreeStrEnum,
)

__version__ = "0.6.0"

__all__ = (
    "CaseInsensitiveStrEnum",
    "DoubleSidedCaseInsensitiveStrEnum",
    "DoubleSidedStrEnum",
    "DuplicateFreeStrEnum",
    "StrEnum",
    "__version__",
)
