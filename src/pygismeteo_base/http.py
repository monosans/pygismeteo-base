from __future__ import annotations

from typing import Final, Generic, Optional

from pydantic import AnyHttpUrl, SecretStr, validate_call
from typing_extensions import Any, TypeVar

from pygismeteo_base import types

T = TypeVar("T")


class BaseHttpClient(Generic[T]):
    __slots__ = ("base_url", "lang", "session", "token")

    @validate_call(config={"arbitrary_types_allowed": True})
    def __init__(
        self,
        *,
        token: str,
        base_url: AnyHttpUrl,
        lang: types.Lang,
        session: Optional[T],
    ) -> None:
        self.token: Final = SecretStr(token)
        self.base_url: Final = base_url
        self.lang: Final = lang
        self.session = session

    def _get_params_and_headers(
        self, params: types.Params, /
    ) -> tuple[types.Params, dict[str, str]]:
        params["lang"] = self.lang
        return params, {
            "Accept": "application/json",
            "X-Gismeteo-Token": self.token.get_secret_value(),
        }


THttpClient = TypeVar("THttpClient", bound=BaseHttpClient[Any])
