from __future__ import annotations

from typing import Final, Generic

from pygismeteo_base import http


class EndpointABC(Generic[http.THttpClient]):
    __slots__ = ("_session",)

    def __init__(self, session: http.THttpClient) -> None:
        self._session: Final = session
