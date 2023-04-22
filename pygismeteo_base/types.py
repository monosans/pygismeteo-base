from __future__ import annotations

from typing import Mapping, Optional, Type, TypeVar, Union

from . import models
from .typing_compat import Literal, TypeAlias

Lang: TypeAlias = Literal["ru", "en", "ua", "lt", "lv", "pl", "ro"]
"""Языки, поддерживаемые Gismeteo API."""
Step3Days: TypeAlias = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""Допустимые значения аргумента days у погоды с шагом 3 часа."""
Step6or24Days: TypeAlias = Literal[3, 4, 5, 6, 7, 8, 9, 10]
Step6Days: TypeAlias = Step6or24Days
"""Допустимые значения аргумента days у погоды с шагом 6 часов."""
Step24Days: TypeAlias = Step6or24Days
"""Допустимые значения аргумента days у погоды с шагом 24 часа."""
StepNDays: TypeAlias = Union[Step3Days, Step6Days, Step24Days]
Params: TypeAlias = Optional[Mapping[str, str]]
Headers: TypeAlias = Optional[Mapping[str, str]]
SearchLimit: TypeAlias = Literal[
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
]
"""Допустимые значения аргумента limit у поиска по координатам."""

StepNModel: TypeAlias = Type[
    Union[models.step3.Model, models.step6.Model, models.step24.Model]
]
TDays = TypeVar("TDays", Step3Days, Step6Days, Step24Days)
TStepNModel = TypeVar(
    "TStepNModel", models.step3.Model, models.step6.Model, models.step24.Model
)
TStepNModelItem = TypeVar(
    "TStepNModelItem",
    models.step3.ModelItem,
    models.step6.ModelItem,
    models.step24.ModelItem,
)
