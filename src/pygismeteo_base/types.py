from __future__ import annotations

from collections.abc import MutableMapping
from typing import Annotated, Union

from pydantic import Field
from typing_extensions import TypeAlias

from pygismeteo_base._enum import StrEnum

Params: TypeAlias = MutableMapping[str, str]


class Lang(StrEnum):
    """Поддерживаемые Gismeteo API языки."""

    RU = "ru"
    EN = "en"
    UA = "ua"
    LT = "lt"
    LV = "lv"
    PL = "pl"
    RO = "ro"


LocalityID: TypeAlias = Annotated[int, Field(ge=1)]
"""ID географического объекта."""
Latitude: TypeAlias = Annotated[Union[int, float], Field(ge=-90, le=90)]
"""Широта."""
Longitude: TypeAlias = Annotated[Union[int, float], Field(ge=-180, le=180)]
"""Долгота."""
SearchLimit: TypeAlias = Annotated[int, Field(ge=1, le=36)]
"""Ограничение количества географических объектов у поиска по координатам."""

Step3Days: TypeAlias = Annotated[int, Field(ge=1, le=10)]
"""Количество дней у погоды с шагом 3 часа."""
Step6Days: TypeAlias = Annotated[int, Field(ge=3, le=10)]
"""Количество дней у погоды с шагом 6 часов."""
Step24Days: TypeAlias = Annotated[int, Field(ge=3, le=10)]
"""Количество дней у погоды с шагом 24 часа."""
