from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Type

from pydantic import TypeAdapter
from typing_extensions import override

from .. import models, types, validators


class StepNMixin(metaclass=ABCMeta):
    __slots__ = ()

    @staticmethod
    @abstractmethod
    def _endpoint() -> str:
        pass

    @staticmethod
    @abstractmethod
    def _model() -> types.StepNResponse:
        pass

    @staticmethod
    @abstractmethod
    def _days_validator() -> TypeAdapter[int]:
        pass


class Step3Mixin(StepNMixin):
    __slots__ = ()

    @staticmethod
    @override
    def _endpoint() -> str:
        return "weather/forecast"

    @staticmethod
    @override
    def _model() -> Type[models.step3.Response]:
        return models.step3.Response

    @staticmethod
    @override
    def _days_validator() -> TypeAdapter[int]:
        return validators.Step3Days


class Step6Mixin(StepNMixin):
    __slots__ = ()

    @staticmethod
    @override
    def _endpoint() -> str:
        return "weather/forecast/by_day_part"

    @staticmethod
    @override
    def _model() -> Type[models.step6.Response]:
        return models.step6.Response

    @staticmethod
    @override
    def _days_validator() -> TypeAdapter[int]:
        return validators.Step6Days


class Step24Mixin(StepNMixin):
    __slots__ = ()

    @staticmethod
    @override
    def _endpoint() -> str:
        return "weather/forecast/aggregate"

    @staticmethod
    @override
    def _model() -> Type[models.step24.Response]:
        return models.step24.Response

    @staticmethod
    @override
    def _days_validator() -> TypeAdapter[int]:
        return validators.Step24Days
