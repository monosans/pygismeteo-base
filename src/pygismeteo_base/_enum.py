from __future__ import annotations

import enum
from typing import Any, Self


class IntEnum(enum.IntEnum):
    def __new__(cls, value: int, *_: Any) -> Self:
        member = int.__new__(cls, value)
        member._value_ = value
        return member


class StrEnum(enum.StrEnum):
    def __new__(cls, value: str, *_: Any) -> Self:
        member = str.__new__(cls, value)
        member._value_ = value
        return member
