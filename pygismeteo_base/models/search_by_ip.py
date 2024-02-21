from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from . import enums


class District(BaseModel):
    name: str
    name_p: str = Field(alias="nameP")


class SubDistrict(BaseModel):
    name: str
    name_p: str = Field(alias="nameP")


class Country(BaseModel):
    name: str
    code: str
    name_p: str = Field(alias="nameP")


class Model(BaseModel):
    district: Optional[District] = None
    id: int
    sub_district: Optional[SubDistrict] = None
    url: str
    name_p: str = Field(alias="nameP")
    name: str
    kind: enums.GeographicObjectType
    country: Country


class Response(BaseModel):
    response: Model
