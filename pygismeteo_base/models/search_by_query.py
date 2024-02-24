from __future__ import annotations

from typing import Optional, Tuple

from pydantic import ConfigDict, Field, RootModel

from . import enums
from ._base import FrozenModel


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


class Model(RootModel[Tuple[ModelItem, ...]]):
    model_config = ConfigDict(frozen=True)


class Items(FrozenModel):
    items: Model = Field(default_factory=lambda: Model(()))


class Response(FrozenModel):
    response: Items
