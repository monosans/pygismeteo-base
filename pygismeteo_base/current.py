from __future__ import annotations

from typing import Tuple

from . import http, types, validators
from .endpoint import EndpointABC


class CurrentBase(EndpointABC[http.THttpClient]):
    __slots__ = ()

    @property
    def _endpoint(self) -> str:
        return "weather/current"

    def _get_params_by_coordinates(
        self, latitude: float, longitude: float
    ) -> Tuple[str, types.Params]:
        coords_validator = validators.Coordinates(
            latitude=latitude, longitude=longitude
        )
        params = {
            "latitude": str(coords_validator.latitude),
            "longitude": str(coords_validator.longitude),
        }
        return self._endpoint, params

    def _get_params_by_id(self, id: int) -> Tuple[str, types.Params]:  # noqa: A002
        id_validator = validators.LocalityID.parse_obj(id)
        url = f"{self._endpoint}/{id_validator.__root__}"
        return url, None
