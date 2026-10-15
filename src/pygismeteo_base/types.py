from __future__ import annotations

from collections.abc import MutableMapping
from typing import Annotated, TypeAlias

from pydantic import Field

from pygismeteo_base._enum import StrEnum

Params: TypeAlias = MutableMapping[str, str]


class Lang(StrEnum):
    """Язык названий и описаний в ответах."""

    RU = "ru"
    EN = "en"
    UA = "ua"
    LT = "lt"
    LV = "lv"
    PL = "pl"
    RO = "ro"


LocalityID: TypeAlias = Annotated[int, Field(ge=1)]
"""ID географического объекта из поиска."""
Latitude: TypeAlias = Annotated[int | float, Field(ge=-90, le=90)]
"""Широта, от -90 до 90."""
Longitude: TypeAlias = Annotated[int | float, Field(ge=-180, le=180)]
"""Долгота, от -180 до 180."""
SearchLimit: TypeAlias = Annotated[int, Field(ge=1, le=36)]
"""Сколько объектов вернуть при поиске по координатам, от 1 до 36."""

Step3Days: TypeAlias = Annotated[int, Field(ge=1, le=10)]
"""Количество дней прогноза с шагом 3 часа, от 1 до 10."""
Step6Days: TypeAlias = Annotated[int, Field(ge=3, le=10)]
"""Количество дней прогноза с шагом 6 часов, от 3 до 10."""
Step24Days: TypeAlias = Annotated[int, Field(ge=3, le=10)]
"""Количество дней прогноза с шагом 24 часа, от 3 до 10."""
