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
        coords = validators.Coordinates(latitude=latitude, longitude=longitude)
        return self._endpoint, coords.dict()

    def _get_params_by_id(self, id: int) -> Tuple[str, types.Params]:  # noqa: A002
        locality_id = validators.LocalityID.parse_obj(id)
        url = f"{self._endpoint}/{locality_id.__root__}"
        return url, None
