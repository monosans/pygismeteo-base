from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Tuple, Type, Union

from .. import types, validators


class PeriodABC(metaclass=ABCMeta):
    __slots__ = ()

    @property
    @abstractmethod
    def _endpoint(self) -> str:
        pass


class StepNABC(PeriodABC):
    __slots__ = ()

    def _get_params_by_coordinates(
        self, latitude: float, longitude: float, *, days: Union[str, int]
    ) -> Tuple[str, types.Params]:
        coords = validators.Coordinates(latitude=latitude, longitude=longitude)
        days_model = self._days_validator.parse_obj(days)
        params = {"days": days_model.__root__, **coords.dict()}
        return self._endpoint, params

    def _get_params_by_id(
        self,
        # pylint: disable-next=invalid-name,redefined-builtin
        id: int,
        *,
        days: Union[str, int],
    ) -> Tuple[str, types.Params]:
        id_model = validators.LocalityID.parse_obj(id)
        url = f"{self._endpoint}/{id_model.__root__}"
        days_model = self._days_validator.parse_obj(days)
        params = {"days": days_model.__root__}
        return url, params

    @property
    @abstractmethod
    def _days_validator(
        self,
    ) -> Type[Union[validators.Step3Days, validators.Step6or24Days]]:
        pass
