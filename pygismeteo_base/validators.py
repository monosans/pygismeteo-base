# -*- coding: utf-8 -*-
from ipaddress import IPv4Address
from typing import Optional

from pydantic import BaseModel, Field

import pygismeteo_base


class Settings(BaseModel):
    lang: Optional[pygismeteo_base.types.LANG]
    token: Optional[str]

    class Config:
        anystr_strip_whitespace = True


class Coordinates(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)


class Limit(BaseModel):
    __root__: int = Field(..., ge=1, le=36)


class IPAddress(BaseModel):
    __root__: IPv4Address


class Query(BaseModel):
    __root__: str

    class Config:
        anystr_strip_whitespace = True


class LocalityID(BaseModel):
    __root__: int


class Days3to10(BaseModel):
    __root__: int = Field(..., ge=3, le=10)


class Days1to10(BaseModel):
    __root__: int = Field(..., ge=1, le=10)
