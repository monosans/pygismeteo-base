from __future__ import annotations

from typing import Type

from .. import models, validators
from . import mixins_abc


class CurrentMixin(mixins_abc.PeriodMixin):
    __slots__ = ()

    @property
    def _endpoint(self) -> str:
        return "weather/current"

    @property
    def _model(self) -> Type[models.current.Model]:
        return models.current.Model


class Step3Mixin(mixins_abc.StepNMixin):
    __slots__ = ()

    @property
    def _endpoint(self) -> str:
        return "weather/forecast"

    @property
    def _model(self) -> Type[models.step3.Model]:
        return models.step3.Model

    @property
    def _days_validator(self) -> Type[validators.Step3Days]:
        return validators.Step3Days


class Step6Mixin(mixins_abc.StepNMixin):
    __slots__ = ()

    @property
    def _endpoint(self) -> str:
        return "weather/forecast/by_day_part"

    @property
    def _model(self) -> Type[models.step6.Model]:
        return models.step6.Model

    @property
    def _days_validator(self) -> Type[validators.Step6or24Days]:
        return validators.Step6or24Days


class Step24Mixin(mixins_abc.StepNMixin):
    __slots__ = ()

    @property
    def _endpoint(self) -> str:
        return "weather/forecast/aggregate"

    @property
    def _model(self) -> Type[models.step24.Model]:
        return models.step24.Model

    @property
    def _days_validator(self) -> Type[validators.Step6or24Days]:
        return validators.Step6or24Days
