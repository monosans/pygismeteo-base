from __future__ import annotations

from abc import abstractmethod
from typing import Tuple, Type, Union

from .. import http, types, validators
from ..endpoint import EndpointABC


class StepNABC(EndpointABC[http.THttpClient]):
    __slots__ = ()

    @property
    @abstractmethod
    def _model(self) -> types.StepNModel:
        pass

    @property
    @abstractmethod
    def _days_validator(
        self,
    ) -> Type[Union[validators.Step3Days, validators.Step6Days, validators.Step24Days]]:
        pass

    def _get_params_by_coordinates(
        self, latitude: float, longitude: float, *, days: types.StepNDays
    ) -> Tuple[str, types.Params]:
        coords_validator = validators.Coordinates(
            latitude=latitude, longitude=longitude
        )
        days_validator = self._days_validator.parse_obj(days)
        params = {
            "latitude": str(coords_validator.latitude),
            "longitude": str(coords_validator.longitude),
            "days": str(days_validator.__root__),
        }
        return self._endpoint, params

    def _get_params_by_id(
        self, id: int, *, days: types.StepNDays  # noqa: A002
    ) -> Tuple[str, types.Params]:
        id_validator = validators.LocalityID.parse_obj(id)
        url = f"{self._endpoint}/{id_validator.__root__}"
        days_validator = self._days_validator.parse_obj(days)
        params = {"days": str(days_validator.__root__)}
        return url, params
