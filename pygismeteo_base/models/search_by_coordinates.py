# -*- coding: utf-8 -*-
from typing import Iterator as _Iterator
from typing import List as _List
from typing import Optional as _Optional

from pydantic import BaseModel as _BaseModel
from pydantic import Field as _Field


class District(_BaseModel):
    name: str
    name_p: str = _Field(..., alias="nameP")


class SubDistrict(_BaseModel):
    name: str
    name_p: str = _Field(..., alias="nameP")


class Country(_BaseModel):
    name: _Optional[str]
    code: str
    name_p: _Optional[str] = _Field(..., alias="nameP")


class ModelItem(_BaseModel):
    district: _Optional[District]
    id: int
    sub_district: _Optional[SubDistrict]
    url: str
    name_p: _Optional[str] = _Field(..., alias="nameP")
    name: _Optional[str]
    distance: float
    kind: str
    country: Country


class Model(_BaseModel):
    __root__: _List[ModelItem]

    def __iter__(self) -> _Iterator[ModelItem]:  # type: ignore[override]
        return iter(self.__root__)

    def __getitem__(self, item: int) -> ModelItem:
        return self.__root__[item]
