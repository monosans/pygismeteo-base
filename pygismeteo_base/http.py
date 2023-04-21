from __future__ import annotations

from typing import Any, Generic, Optional, Tuple, TypeVar

from . import constants, types, validators

T = TypeVar("T")


class BaseHttpClient(Generic[T]):
    __slots__ = ("session", "settings")

    def __init__(self, session: Optional[T], settings: validators.Settings) -> None:
        self.session = session
        self.settings = settings

    def _get_params_and_headers(
        self, params: types.Params
    ) -> Tuple[types.Params, types.Headers]:
        if self.settings.lang:
            params = (
                {"lang": self.settings.lang, **params}
                if params
                else {"lang": self.settings.lang}
            )
        token = self.settings.token or constants.DEFAULT_TOKEN
        headers = {"X-Gismeteo-Token": token}
        return params, headers


THttpClient = TypeVar("THttpClient", bound=BaseHttpClient[Any])
