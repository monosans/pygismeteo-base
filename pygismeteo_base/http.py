from __future__ import annotations

from typing import Any, Generic, Optional, Tuple, TypeVar

from . import constants, types, validators

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
    ) -> Tuple[types.Params, types.Headers]:
        lang_dict = {"lang": self.settings.lang} if self.settings.lang else {}
        params_dict = params or {}
        token = self.settings.token or constants.DEFAULT_TOKEN
        return {**lang_dict, **params_dict}, {"X-Gismeteo-Token": token}


# pylint: disable-next=invalid-name
THttpClient = TypeVar("THttpClient", bound=BaseHttpClient[Any])
