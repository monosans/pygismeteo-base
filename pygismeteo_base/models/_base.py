from __future__ import annotations

from pydantic import BaseModel, RootModel
from pydantic.root_model import RootModelRootType


class FrozenModel(BaseModel):
    model_config = {"frozen": True}


class FrozenRootModel(RootModel[RootModelRootType]):
    model_config = {"frozen": True}  # noqa: RUF012
