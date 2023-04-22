from __future__ import annotations

from ipaddress import IPv4Address
from typing import Union

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
        coords_validator = validators.Coordinates(
            latitude=latitude, longitude=longitude
        )
        limit_validator = validators.SearchLimit.parse_obj(limit)
        return {
            "latitude": str(coords_validator.latitude),
            "longitude": str(coords_validator.longitude),
            "limit": str(limit_validator.__root__),
        }

    @staticmethod
    def _get_params_by_ip(ip: Union[IPv4Address, str]) -> types.Params:
        ip_validator = validators.IPAddress.parse_obj(ip)
        return {"ip": str(ip_validator.__root__)}

    @staticmethod
    def _get_params_by_query(query: str) -> types.Params:
        query_validator = validators.Query.parse_obj(query)
        return {"query": query_validator.__root__}
