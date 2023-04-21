from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Type, Union

from .. import models, types, validators


class StepNMixin(metaclass=ABCMeta):
    __slots__ = ()

    @property
    @abstractmethod
    def _endpoint(self) -> str:
        pass

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


class Step3Mixin(StepNMixin):
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


class Step6Mixin(StepNMixin):
    __slots__ = ()

    @property
    def _endpoint(self) -> str:
        return "weather/forecast/by_day_part"

    @property
    def _model(self) -> Type[models.step6.Model]:
        return models.step6.Model

    @property
    def _days_validator(self) -> Type[validators.Step6Days]:
        return validators.Step6Days


class Step24Mixin(StepNMixin):
    __slots__ = ()

    @property
    def _endpoint(self) -> str:
        return "weather/forecast/aggregate"

    @property
    def _model(self) -> Type[models.step24.Model]:
        return models.step24.Model

    @property
    def _days_validator(self) -> Type[validators.Step24Days]:
        return validators.Step24Days
