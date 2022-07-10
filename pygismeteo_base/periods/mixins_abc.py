from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any

from pygismeteo_base import validators


class PeriodMixin(metaclass=ABCMeta):
    __slots__ = ()

    @property
    @abstractmethod
    def _model(self) -> type[Any]:
        pass

    @property
    @abstractmethod
    def _endpoint(self) -> str:
        pass


class StepNMixin(PeriodMixin):
    __slots__ = ()

    @property
    @abstractmethod
    def _days_validator(
        self,
    ) -> type[validators.Step3Days | validators.Step6or24Days]:
        pass
