from __future__ import annotations

from typing import Final

from pydantic import validate_call

from pygismeteo_base import http, types
from pygismeteo_base.endpoints._base import EndpointABC


class Step6Base(EndpointABC[http.THttpClient]):
    __slots__ = ()

    _endpoint: Final = "weather/forecast/by_day_part"

    @classmethod
    @validate_call(config={"arbitrary_types_allowed": True})
    def _get_params_by_coordinates(
        cls,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        days: types.Step6Days,
    ) -> tuple[str, dict[str, str]]:
        return cls._endpoint, {
            "latitude": str(latitude),
            "longitude": str(longitude),
            "days": str(days),
        }

    @classmethod
    @validate_call(config={"arbitrary_types_allowed": True})
    def _get_params_by_id(
        cls, id_: types.LocalityID, /, *, days: types.Step6Days
    ) -> tuple[str, dict[str, str]]:
        return f"{cls._endpoint}/{id_}", {"days": str(days)}
