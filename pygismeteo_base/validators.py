from __future__ import annotations

import ipaddress
from typing import Optional

from pydantic import BaseModel, ConfigDict, TypeAdapter

from . import types


class Settings(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True, validate_assignment=True
    )

    lang: Optional[types.Lang]
    token: str


IPv4Address = TypeAdapter(ipaddress.IPv4Address)
Latitude = TypeAdapter(types.Latitude)
LocalityID = TypeAdapter(types.LocalityID)
Longitude = TypeAdapter(types.Longitude)

Step3Days = TypeAdapter(types.Step3Days)
Step6or24Days = TypeAdapter(types.Step6or24Days)
Step6Days = Step6or24Days
Step24Days = Step6or24Days
