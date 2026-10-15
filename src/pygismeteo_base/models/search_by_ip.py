"""Поиск по IP-адресу. Запрос возвращает `Model`."""

from __future__ import annotations

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


class Model(FrozenModel):
    """Географический объект, к которому относится IP-адрес."""

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
    kind: enums.GeographicObjectType
    country: Country
