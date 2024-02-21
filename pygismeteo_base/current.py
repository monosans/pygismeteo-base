from __future__ import annotations

from typing import Dict, Tuple

from pydantic import validate_call
from typing_extensions import override

from . import http, types
from .endpoint import EndpointABC


class CurrentBase(EndpointABC[http.THttpClient]):
    __slots__ = ()

    @staticmethod
    @override
    def _endpoint() -> str:
        return "weather/current"

    @validate_call
    def _get_params_by_coordinates(
        self, latitude: types.Latitude, longitude: types.Longitude
    ) -> Tuple[str, Dict[str, str]]:
        return self._endpoint(), {
            "latitude": str(latitude),
            "longitude": str(longitude),
        }

    @validate_call
    def _get_params_by_id(
        self,
        id: types.LocalityID,  # noqa: A002
    ) -> Tuple[str, None]:
        return f"{self._endpoint()}/{id}", None
