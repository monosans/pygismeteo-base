# -*- coding: utf-8 -*-
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


class Model(_BaseModel):
    district: _Optional[District]
    id: int
    sub_district: _Optional[SubDistrict]
    url: str
    name_p: _Optional[str] = _Field(..., alias="nameP")
    name: _Optional[str]
    kind: str
    country: Country
