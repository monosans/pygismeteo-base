from __future__ import annotations

from typing import Final

from pydantic import validate_call

from pygismeteo_base import http, types
from pygismeteo_base.endpoints._base import EndpointABC


class CurrentBase(EndpointABC[http.THttpClient]):
    __slots__ = ()

    _endpoint: Final = "weather/current"

    @classmethod
    @validate_call(config={"arbitrary_types_allowed": True})
    def _get_params_by_coordinates(
        cls, latitude: types.Latitude, longitude: types.Longitude
    ) -> tuple[str, dict[str, str]]:
        return cls._endpoint, {
            "latitude": str(latitude),
            "longitude": str(longitude),
        }

    @classmethod
    @validate_call(config={"arbitrary_types_allowed": True})
    def _get_params_by_id(
        cls, id_: types.LocalityID, /
    ) -> tuple[str, dict[str, str]]:
        return f"{cls._endpoint}/{id_}", {}
