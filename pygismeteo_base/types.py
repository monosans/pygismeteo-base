from __future__ import annotations

from typing import MutableMapping, Optional, Type, Union

import annotated_types as at
from typing_extensions import Annotated, Literal, TypeAlias, TypeVar

from . import models

Params: TypeAlias = Optional[MutableMapping[str, str]]

Lang: TypeAlias = Literal["ru", "en", "ua", "lt", "lv", "pl", "ro"]
"""Поддерживаемые Gismeteo API языки."""
LocalityID: TypeAlias = Annotated[int, at.Ge(1)]
"""ID географического объекта."""
Latitude: TypeAlias = Annotated[Union[int, float], at.Ge(-90), at.Le(90)]
"""Широта."""
Longitude: TypeAlias = Annotated[Union[int, float], at.Ge(-180), at.Le(180)]
"""Долгота."""
SearchLimit: TypeAlias = Annotated[int, at.Ge(1), at.Le(36)]
"""Ограничение количества географических объектов у поиска по координатам."""

Step6or24Days: TypeAlias = Annotated[int, at.Ge(3), at.Le(10)]
Step3Days: TypeAlias = Annotated[int, at.Ge(1), at.Le(10)]
"""Количество дней у погоды с шагом 3 часа."""
Step6Days: TypeAlias = Step6or24Days
"""Количество дней у погоды с шагом 6 часов."""
Step24Days: TypeAlias = Step6or24Days
"""Количество дней у погоды с шагом 24 часа."""
StepNDays: TypeAlias = Union[Step3Days, Step6Days, Step24Days]
StepNResponse: TypeAlias = Type[
    Union[models.step3.Response, models.step6.Response, models.step24.Response]
]

TStepNDays = TypeVar("TStepNDays", Step3Days, Step6Days, Step24Days)
TStepNModel = TypeVar(
    "TStepNModel", models.step3.Model, models.step6.Model, models.step24.Model
)
TStepNModelItem = TypeVar(
    "TStepNModelItem",
    models.step3.ModelItem,
    models.step6.ModelItem,
    models.step24.ModelItem,
)
