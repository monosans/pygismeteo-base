from __future__ import annotations

from typing import Tuple

from . import constants, types, validators


class BaseHttpClient:
    __slots__ = ("settings",)

    def __init__(self, settings: validators.Settings) -> None:
        self.settings = settings

    def _get_params_and_headers(
        self, params: types.Params
    ) -> Tuple[types.Params, types.Headers]:
        lang_dict = {"lang": self.settings.lang} if self.settings.lang else {}
        params_dict = params or {}
        token = self.settings.token or constants.DEFAULT_TOKEN
        return {**lang_dict, **params_dict}, {"X-Gismeteo-Token": token}
