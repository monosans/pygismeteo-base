from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any, Type, Union

from .. import validators


class PeriodMixin(metaclass=ABCMeta):
    __slots__ = ()

    @property
    @abstractmethod
    def _model(self) -> Type[Any]:
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
    ) -> Type[Union[validators.Step3Days, validators.Step6or24Days]]:
        pass
