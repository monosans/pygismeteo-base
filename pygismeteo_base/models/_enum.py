from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, List

from typing_extensions import Any, Self, override


class IntEnum(int, Enum):
    if TYPE_CHECKING:
        _value_: int

        @property
        @override
        def value(self) -> int: ...

        def __new__(cls, value: int) -> Self: ...
    else:

        def __new__(cls, value: int, *_: Any) -> Self:
            member = int.__new__(cls, value)
            member._value_ = value
            return member

    __str__ = int.__str__ if int.__str__ is not object.__str__ else int.__repr__
    __format__ = int.__format__  # type: ignore[assignment]


class StrEnum(str, Enum):
    if TYPE_CHECKING:
        _value_: str

        @property
        @override
        def value(self) -> str: ...

        def __new__(cls, value: str) -> Self: ...
    else:

        def __new__(cls, value: str, *_: Any) -> Self:
            member = str.__new__(cls, value)
            member._value_ = value
            return member

    @staticmethod
    @override
    def _generate_next_value_(
        name: str, start: int, count: int, last_values: List[str]
    ) -> str:
        return name

    __str__ = str.__str__ if str.__str__ is not object.__str__ else str.__repr__
    __format__ = str.__format__  # type: ignore[assignment]
