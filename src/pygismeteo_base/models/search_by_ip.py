"""Поиск по IP-адресу. Запрос возвращает `Model`."""

from __future__ import annotations

from pydantic import Field

from pygismeteo_base.models import enums
from pygismeteo_base.models._base import FrozenModel


class District(FrozenModel):
    name: str
    name_p: str = Field(alias="nameP")


class SubDistrict(FrozenModel):
    name: str
    name_p: str = Field(alias="nameP")


class Country(FrozenModel):
    """Страна."""

    name: str
    code: str
    name_p: str = Field(alias="nameP")


class Model(FrozenModel):
    """Географический объект, к которому относится IP-адрес."""

    district: District | None = None
    id: int
    """ID для запросов погоды."""
    sub_district: SubDistrict | None = None
    url: str
    name_p: str = Field(alias="nameP")
    name: str
    kind: enums.GeographicObjectType
    country: Country
