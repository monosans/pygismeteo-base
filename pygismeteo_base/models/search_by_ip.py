from __future__ import annotations

from typing import Optional

try:
    from pydantic.v1 import BaseModel, Field
except ImportError:
    from pydantic import BaseModel, Field  # type: ignore[assignment]


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


class Model(BaseModel):
    district: Optional[District] = None
    id: int
    sub_district: Optional[SubDistrict] = None
    url: str
    name_p: Optional[str] = Field(default=None, alias="nameP")
    name: Optional[str] = None
    kind: str
    country: Country
