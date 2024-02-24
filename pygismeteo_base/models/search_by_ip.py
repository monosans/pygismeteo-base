from __future__ import annotations

from typing import Optional

from pydantic import Field

from . import enums
from ._base import FrozenModel


class District(FrozenModel):
    name: str
    name_p: str = Field(alias="nameP")


class SubDistrict(FrozenModel):
    name: str
    name_p: str = Field(alias="nameP")


class Country(FrozenModel):
    name: str
    code: str
    name_p: str = Field(alias="nameP")


class Model(FrozenModel):
    district: Optional[District] = None
    id: int
    sub_district: Optional[SubDistrict] = None
    url: str
    name_p: str = Field(alias="nameP")
    name: str
    kind: enums.GeographicObjectType
    country: Country


class Response(FrozenModel):
    response: Model
