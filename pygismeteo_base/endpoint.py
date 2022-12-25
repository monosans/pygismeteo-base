from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Generic

from . import http


class EndpointABC(Generic[http.THttpClient], metaclass=ABCMeta):
    __slots__ = ("_session",)

    def __init__(self, session: http.THttpClient) -> None:
        self._session = session

    @property
    @abstractmethod
    def _endpoint(self) -> str:
        pass
