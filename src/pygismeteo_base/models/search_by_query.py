from __future__ import annotations

from typing import Optional

from pydantic import Field
from typing_extensions import TypeAlias

from pygismeteo_base.models import enums
from pygismeteo_base.models._base import FrozenModel


class District(FrozenModel):
    name: str
    name_p: Optional[str] = Field(default=None, alias="nameP")


class Country(FrozenModel):
    name: str
    code: str
    name_p: Optional[str] = Field(default=None, alias="nameP")


class SubDistrict(FrozenModel):
    name: str
    name_p: Optional[str] = Field(default=None, alias="nameP")


class ModelItem(FrozenModel):
    district: Optional[District] = None
    id: int
    sub_district: Optional[SubDistrict] = None
    url: str
    name_p: Optional[str] = Field(default=None, alias="nameP")
    name: str
    rate: int
    weight: int
    kind: enums.GeographicObjectType
    country: Country


Model: TypeAlias = tuple[ModelItem, ...]
