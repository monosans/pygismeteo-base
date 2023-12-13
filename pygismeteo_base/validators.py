from __future__ import annotations

from ipaddress import IPv4Address
from typing import Optional

from . import types
from ._pydantic import BaseModel, Field, FrozenModel


class Settings(BaseModel):
    lang: Optional[types.Lang] = Field(...)
    token: str = Field(...)

    class Config:
        anystr_strip_whitespace = True
        validate_assignment = True


class Coordinates(FrozenModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class SearchLimit(FrozenModel):
    __root__: int = Field(ge=1, le=36)


class IPAddress(FrozenModel):
    __root__: IPv4Address


class Query(FrozenModel):
    __root__: str


class LocalityID(FrozenModel):
    __root__: int = Field(ge=1)


class Step3Days(FrozenModel):
    __root__: int = Field(ge=1, le=10)


class Step6or24Days(FrozenModel):
    __root__: int = Field(ge=3, le=10)


Step6Days = Step6or24Days
Step24Days = Step6or24Days
