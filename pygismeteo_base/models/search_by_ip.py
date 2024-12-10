from __future__ import annotations

from typing import Final, Optional

from pydantic import Field, TypeAdapter
from typing_extensions import TypedDict

from pygismeteo_base.models import enums
from pygismeteo_base.models._base import FrozenModel


class District(FrozenModel):
    name: str
    name_p: str = Field(alias="nameP")


class SubDistrict(FrozenModel):
    name: str
    name_p: str = Field(alias="nameP")


class Country(FrozenModel):
    name: str
    code: str
    name_p: str = Field(alias="nameP")


class Model(FrozenModel):
    district: Optional[District] = None
    id: int
    sub_district: Optional[SubDistrict] = None
    url: str
    name_p: str = Field(alias="nameP")
    name: str
    kind: enums.GeographicObjectType
    country: Country


class _Response(TypedDict):
    response: Model


response_adapter: Final = TypeAdapter(_Response, config={"frozen": True})
