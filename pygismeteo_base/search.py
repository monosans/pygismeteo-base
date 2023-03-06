from __future__ import annotations

from . import http, types, validators
from .endpoint import EndpointABC


class SearchBase(EndpointABC[http.THttpClient]):
    __slots__ = ()

    @property
    def _endpoint(self) -> str:
        return "search/cities"

    @staticmethod
    def _get_params_by_coordinates(
        latitude: float, longitude: float, *, limit: types.SearchLimit
    ) -> types.Params:
        coordinates = validators.Coordinates(latitude=latitude, longitude=longitude)
        params = coordinates.dict()
        lim = validators.SearchLimit.parse_obj(limit).__root__
        return dict(params, limit=lim)

    @staticmethod
    def _get_params_by_ip(ip: str) -> types.Params:
        ip = str(validators.IPAddress.parse_obj(ip).__root__)
        return {"ip": ip}

    @staticmethod
    def _get_params_by_query(query: str) -> types.Params:
        query = validators.Query.parse_obj(query).__root__
        return {"query": query}
