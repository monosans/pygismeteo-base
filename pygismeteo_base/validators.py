from __future__ import annotations

from ipaddress import IPv4Address
from typing import Optional

from pydantic import BaseModel, Field

from . import types


class Settings(BaseModel):
    lang: Optional[types.Lang] = Field(...)
    token: Optional[str] = Field(...)

    class Config:
        anystr_strip_whitespace = True
        validate_assignment = True


class Coordinates(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class SearchLimit(BaseModel):
    __root__: int = Field(ge=1, le=36)


class IPAddress(BaseModel):
    __root__: IPv4Address


class Query(BaseModel):
    __root__: str


class LocalityID(BaseModel):
    __root__: int = Field(ge=1)


class Step3Days(BaseModel):
    __root__: int = Field(ge=1, le=10)


class Step6or24Days(BaseModel):
    __root__: int = Field(ge=3, le=10)


Step6Days = Step6or24Days
Step24Days = Step6or24Days
