# ruff: noqa: FIX002
from __future__ import annotations

from abc import abstractmethod

from pydantic import TypeAdapter

from pygismeteo_base import http, types, validators
from pygismeteo_base.endpoint import EndpointABC


class StepNABC(EndpointABC[http.THttpClient]):
    __slots__ = ()

    @staticmethod
    @abstractmethod
    def _model() -> types.StepNResponse:
        pass

    @staticmethod
    @abstractmethod
    def _days_validator() -> TypeAdapter[int]:
        pass

    def _get_params_by_coordinates(
        self,
        latitude: types.Latitude,
        longitude: types.Longitude,
        *,
        days: types.StepNDays,
    ) -> tuple[str, dict[str, str]]:
        # TODO(monosans): use validate_call when it gets generic support
        # https://github.com/pydantic/pydantic/issues/7796
        return self._endpoint(), {
            "latitude": str(validators.Latitude.validate_python(latitude)),
            "longitude": str(validators.Longitude.validate_python(longitude)),
            "days": str(self._days_validator().validate_python(days)),
        }

    def _get_params_by_id(
        self,
        id: types.LocalityID,  # noqa: A002
        *,
        days: types.StepNDays,
    ) -> tuple[str, dict[str, str]]:
        # TODO(monosans): use validate_call when it gets generic support
        # https://github.com/pydantic/pydantic/issues/7796
        return (
            f"{self._endpoint()}/{validators.LocalityID.validate_python(id)}",
            {"days": str(self._days_validator().validate_python(days))},
        )
