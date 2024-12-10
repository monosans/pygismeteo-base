from __future__ import annotations

from typing import Annotated, Final

from pydantic import Field, TypeAdapter
from typing_extensions import TypedDict

from pygismeteo_base import models


class _CurrentResponse(TypedDict):
    response: models.current.Model


current: Final = TypeAdapter(_CurrentResponse, config={"frozen": True})


class _SearchByCoordinates(TypedDict):
    response: models.search_by_coordinates.Model


search_by_coordinates: Final = TypeAdapter(
    _SearchByCoordinates, config={"frozen": True}
)


class _SearchByIp(TypedDict):
    response: models.search_by_ip.Model


search_by_ip: Final = TypeAdapter(_SearchByIp, config={"frozen": True})


class _SearchByQueryItems(TypedDict):
    items: Annotated[models.search_by_query.Model, Field(default=())]


class _SearchByQuery(TypedDict):
    response: _SearchByQueryItems


search_by_query: Final = TypeAdapter(_SearchByQuery, config={"frozen": True})


class _Step3(TypedDict):
    response: models.step3.Model


step3: Final = TypeAdapter(_Step3, config={"frozen": True})


class _Step6(TypedDict):
    response: models.step6.Model


step6: Final = TypeAdapter(_Step6, config={"frozen": True})


class _Step24(TypedDict):
    response: models.step24.Model


step24: Final = TypeAdapter(_Step24, config={"frozen": True})
