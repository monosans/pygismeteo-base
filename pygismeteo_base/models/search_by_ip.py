from typing import Optional

from pydantic import BaseModel, Field


class District(BaseModel):
    name: str
    name_p: str = Field(..., alias="nameP")


class SubDistrict(BaseModel):
    name: str
    name_p: str = Field(..., alias="nameP")


class Country(BaseModel):
    name: str
    code: str
    name_p: str = Field(..., alias="nameP")


class Model(BaseModel):
    district: Optional[District]
    id: int
    sub_district: Optional[SubDistrict]
    url: str
    name_p: str = Field(..., alias="nameP")
    name: str
    kind: str
    country: Country
