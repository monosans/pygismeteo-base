from __future__ import annotations

from pydantic import BaseModel, Field


class District(BaseModel):
    name: str
    name_p: str = Field(..., alias="nameP")


class SubDistrict(BaseModel):
    name: str
    name_p: str = Field(..., alias="nameP")


class Country(BaseModel):
    name: str | None
    code: str
    name_p: str | None = Field(..., alias="nameP")


class Model(BaseModel):
    district: District | None
    id: int
    sub_district: SubDistrict | None
    url: str
    name_p: str | None = Field(..., alias="nameP")
    name: str | None
    kind: str
    country: Country
