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
    ) -> Type[Union[validators.Step3Days, validators.Step6or24Days]]:
        pass

    def _get_params_by_coordinates(
        self, latitude: float, longitude: float, *, days: Union[str, int]
    ) -> Tuple[str, types.Params]:
        coords = validators.Coordinates(latitude=latitude, longitude=longitude)
        days_model = self._days_validator.parse_obj(days)
        params = dict(coords.dict(), days=days_model.__root__)
        return self._endpoint, params

    def _get_params_by_id(
        self, id: int, *, days: Union[str, int]  # noqa: A002
    ) -> Tuple[str, types.Params]:
        id_model = validators.LocalityID.parse_obj(id)
        url = f"{self._endpoint}/{id_model.__root__}"
        days_model = self._days_validator.parse_obj(days)
        params = {"days": days_model.__root__}
        return url, params
