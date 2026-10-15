"""Поиск по координатам. Запрос возвращает `Model`."""

from __future__ import annotations

from typing import TypeAlias

from pydantic import Field

from pygismeteo_base.models import enums
from pygismeteo_base.models._base import FrozenModel


class District(FrozenModel):
    name: str
    name_p: str = Field(alias="nameP")
    """Название в предложном падеже."""


class SubDistrict(FrozenModel):
    name: str
    name_p: str = Field(alias="nameP")
    """Название в предложном падеже."""


class Country(FrozenModel):
    """Страна."""

    name: str
    code: str
    name_p: str = Field(alias="nameP")
    """Название в предложном падеже."""


class ModelItem(FrozenModel):
    """Географический объект рядом с точкой."""

    district: District | None = None
    """Район."""
    id: int
    """ID для запросов погоды."""
    sub_district: SubDistrict | None = None
    """Подрайон."""
    url: str
    """Путь к странице на сайте, например `/weather-riyadh-5420/`."""
    name_p: str = Field(alias="nameP")
    """Название в предложном падеже."""
    name: str
    distance: float
    """Расстояние до точки поиска."""
    kind: enums.GeographicObjectType
    country: Country


Model: TypeAlias = tuple[ModelItem, ...]
"""Ближайшие объекты."""
