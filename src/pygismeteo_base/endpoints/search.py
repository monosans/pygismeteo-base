from __future__ import annotations

from ipaddress import IPv4Address
from typing import Final

from pydantic import validate_call

from pygismeteo_base import http, types
from pygismeteo_base.endpoints._base import EndpointABC


class SearchBase(EndpointABC[http.THttpClient]):
    __slots__ = ()

    _endpoint: Final = "search/cities"

    @classmethod
    @validate_call(config={"arbitrary_types_allowed": True})
    def _get_params_by_coordinates(
        cls,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        limit: types.SearchLimit,
    ) -> tuple[str, dict[str, str]]:
        return cls._endpoint, {
            "latitude": str(latitude),
            "longitude": str(longitude),
            "limit": str(limit),
        }

    @classmethod
    @validate_call(config={"arbitrary_types_allowed": True})
    def _get_params_by_ip(
        cls, ip: IPv4Address, /
    ) -> tuple[str, dict[str, str]]:
        return cls._endpoint, {"ip": str(ip)}

    @classmethod
    @validate_call(config={"arbitrary_types_allowed": True})
    def _get_params_by_query(cls, query: str, /) -> tuple[str, dict[str, str]]:
        return cls._endpoint, {"query": query}
