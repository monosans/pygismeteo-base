from __future__ import annotations

from collections.abc import MutableMapping
from typing import Annotated, Optional, Union

from pydantic import Field
from typing_extensions import Literal, TypeAlias, TypeVar

from . import models

Params: TypeAlias = Optional[MutableMapping[str, str]]

Lang: TypeAlias = Literal["ru", "en", "ua", "lt", "lv", "pl", "ro"]
"""Поддерживаемые Gismeteo API языки."""
LocalityID: TypeAlias = Annotated[int, Field(ge=1)]
"""ID географического объекта."""
Latitude: TypeAlias = Annotated[Union[int, float], Field(ge=-90, le=90)]
"""Широта."""
Longitude: TypeAlias = Annotated[Union[int, float], Field(ge=-180, le=180)]
"""Долгота."""
SearchLimit: TypeAlias = Annotated[int, Field(ge=1, le=36)]
"""Ограничение количества географических объектов у поиска по координатам."""

Step6or24Days: TypeAlias = Annotated[int, Field(ge=3, le=10)]
Step3Days: TypeAlias = Annotated[int, Field(ge=1, le=10)]
"""Количество дней у погоды с шагом 3 часа."""
Step6Days: TypeAlias = Step6or24Days
"""Количество дней у погоды с шагом 6 часов."""
Step24Days: TypeAlias = Step6or24Days
"""Количество дней у погоды с шагом 24 часа."""
StepNDays: TypeAlias = Union[Step3Days, Step6Days, Step24Days]
StepNResponse: TypeAlias = type[
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
