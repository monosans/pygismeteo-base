from __future__ import annotations

from pygismeteo_base import models, types, validators
from pygismeteo_base.periods import mixins_abc


class CurrentMixin(mixins_abc.PeriodMixin):
    __slots__ = ()

    def _get_params_by_coordinates(
        self, latitude: float, longitude: float
    ) -> tuple[str, types.Params]:
        coords = validators.Coordinates(latitude=latitude, longitude=longitude)
        return self._endpoint, coords.dict()

    def _get_params_by_id(
        self,
        # pylint: disable-next=invalid-name,redefined-builtin
        id: int,
    ) -> tuple[str, types.Params]:
        locality_id = validators.LocalityID.parse_obj(id)
        url = f"{self._endpoint}/{locality_id.__root__}"
        return url, None

    @property
    def _model(self) -> type[models.current.Model]:
        return models.current.Model

    @property
    def _endpoint(self) -> str:
        return "weather/current"


class Step3Mixin(mixins_abc.StepNMixin):
    __slots__ = ()

    @property
    def _days_validator(self) -> type[validators.Step3Days]:
        return validators.Step3Days

    @property
    def _model(self) -> type[models.step3.Model]:
        return models.step3.Model

    @property
    def _endpoint(self) -> str:
        return "weather/forecast"


class Step6Mixin(mixins_abc.StepNMixin):
    __slots__ = ()

    @property
    def _days_validator(self) -> type[validators.Step6or24Days]:
        return validators.Step6or24Days

    @property
    def _model(self) -> type[models.step6.Model]:
        return models.step6.Model

    @property
    def _endpoint(self) -> str:
        return "weather/forecast/by_day_part"


class Step24Mixin(mixins_abc.StepNMixin):
    __slots__ = ()

    @property
    def _days_validator(self) -> type[validators.Step6or24Days]:
        return validators.Step6or24Days

    @property
    def _model(self) -> type[models.step24.Model]:
        return models.step24.Model

    @property
    def _endpoint(self) -> str:
        return "weather/forecast/aggregate"
