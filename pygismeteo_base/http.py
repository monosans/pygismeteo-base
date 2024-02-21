from __future__ import annotations

from typing import Dict, Generic, Optional, Tuple

from typing_extensions import Any, TypeVar

from . import types, validators

T = TypeVar("T")


class BaseHttpClient(Generic[T]):
    __slots__ = ("session", "settings")

    def __init__(
        self, session: Optional[T], settings: validators.Settings
    ) -> None:
        self.session = session
        self.settings = settings

    def _get_params_and_headers(
        self, params: types.Params
    ) -> Tuple[types.Params, Dict[str, str]]:
        if self.settings.lang:
            if params is None:
                params = {"lang": self.settings.lang}
            else:
                params["lang"] = self.settings.lang
        headers = {"X-Gismeteo-Token": self.settings.token}
        return params, headers


THttpClient = TypeVar("THttpClient", bound=BaseHttpClient[Any])
