from __future__ import annotations

from typing import List, Optional

try:
    from pydantic.v1 import BaseModel, Field
except ImportError:  # pragma: no cover
    from pydantic import BaseModel, Field  # type: ignore[assignment]


class District(BaseModel):
    name: str
    name_p: Optional[str] = Field(default=None, alias="nameP")


class Country(BaseModel):
    name: str
    code: str
    name_p: Optional[str] = Field(default=None, alias="nameP")


class SubDistrict(BaseModel):
    name: str
    name_p: Optional[str] = Field(default=None, alias="nameP")


class ModelItem(BaseModel):
    district: Optional[District] = None
    id: int
    sub_district: Optional[SubDistrict] = None
    url: str
    name_p: Optional[str] = Field(default=None, alias="nameP")
    name: str
    rate: int
    weight: int
    kind: str
    country: Country


class Model(BaseModel):
    __root__: List[ModelItem]
