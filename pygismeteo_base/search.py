from __future__ import annotations

from ipaddress import IPv4Address
from typing import Dict, Union

from pydantic import validate_call
from typing_extensions import override

from . import http, types, validators
from .endpoint import EndpointABC


class SearchBase(EndpointABC[http.THttpClient]):
    __slots__ = ()

    @staticmethod
    @override
    def _endpoint() -> str:
        return "search/cities"

    @staticmethod
    @validate_call
    def _get_params_by_coordinates(
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        limit: types.SearchLimit,
    ) -> Dict[str, str]:
        return {
            "latitude": str(latitude),
            "longitude": str(longitude),
            "limit": str(limit),
        }

    @staticmethod
    def _get_params_by_ip(ip: Union[IPv4Address, str]) -> Dict[str, str]:
        return {"ip": str(validators.IPv4Address.validate_python(ip))}

    @staticmethod
    @validate_call
    def _get_params_by_query(query: str) -> Dict[str, str]:
        return {"query": query}
