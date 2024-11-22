from __future__ import annotations

from stringenum._compat import StrEnum
from stringenum._core import (
    CaseInsensitiveStrEnum,
    DoubleSidedCaseInsensitiveStrEnum,
    DoubleSidedStrEnum,
    DuplicateFreeStrEnum,
)

__version__ = "0.4.0"

__all__ = (
    "StrEnum",
    "CaseInsensitiveStrEnum",
    "DoubleSidedCaseInsensitiveStrEnum",
    "DoubleSidedStrEnum",
    "DuplicateFreeStrEnum",
    "__version__",
)
