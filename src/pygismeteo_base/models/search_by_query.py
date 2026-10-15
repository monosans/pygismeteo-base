"""Поиск по названию. Ответ — `Model`."""

from __future__ import annotations

from typing import TypeAlias

from pydantic import Field

from pygismeteo_base.models import enums
from pygismeteo_base.models._base import FrozenModel


class District(FrozenModel):
    name: str
    name_p: str | None = Field(default=None, alias="nameP")


class Country(FrozenModel):
    """Страна."""

    name: str
    code: str
    name_p: str | None = Field(default=None, alias="nameP")


class SubDistrict(FrozenModel):
    name: str
    name_p: str | None = Field(default=None, alias="nameP")


class ModelItem(FrozenModel):
    """Найденный географический объект."""

    district: District | None = None
    id: int
    """ID для запросов погоды."""
    sub_district: SubDistrict | None = None
    url: str
    name_p: str | None = Field(default=None, alias="nameP")
    name: str
    rate: int
    weight: int
    kind: enums.GeographicObjectType
    country: Country


Model: TypeAlias = tuple[ModelItem, ...]
"""Найденные объекты; пустой, если ничего не найдено."""
