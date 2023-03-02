from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class District(BaseModel):
    name: str
    name_p: str = Field(alias="nameP")


class SubDistrict(BaseModel):
    name: str
    name_p: str = Field(alias="nameP")


class Country(BaseModel):
    name: Optional[str] = None
    code: str
    name_p: Optional[str] = Field(default=None, alias="nameP")


class ModelItem(BaseModel):
    district: Optional[District] = None
    id: int
    sub_district: Optional[SubDistrict] = None
    url: str
    name_p: Optional[str] = Field(default=None, alias="nameP")
    name: Optional[str] = None
    distance: float
    kind: str
    country: Country


class Model(BaseModel):
    __root__: List[ModelItem]
