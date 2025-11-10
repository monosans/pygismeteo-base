from __future__ import annotations

from typing import TypeAlias

from pydantic import Field

from pygismeteo_base.models import enums
from pygismeteo_base.models._base import FrozenModel


class Precipitation(FrozenModel):
    type_ext: int | None = None
    intensity: enums.PrecipitationIntensity
    correction: bool | None = None
    amount: float | None = None
    duration: int
    type: enums.PrecipitationType


class Pressure(FrozenModel):
    h_pa: int
    mm_hg_atm: int
    in_hg: float


class Humidity(FrozenModel):
    percent: int | None = None


class Direction(FrozenModel):
    degree: int | None = None
    scale_8: enums.WindScale8 | None = None


class Speed(FrozenModel):
    km_h: int
    m_s: int
    mi_h: int


class Wind(FrozenModel):
    direction: Direction
    speed: Speed


class Cloudiness(FrozenModel):
    type: enums.CloudinessType
    percent: int


class Date(FrozenModel):
    utc: str = Field(alias="UTC")
    time_zone_offset: int
    local: str
    hr_to_forecast: int | None = None
    unix: int


class Radiation(FrozenModel):
    uvb_index: int | None = None
    uvb: int = Field(alias="UVB")


class Comfort(FrozenModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Water(FrozenModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Air(FrozenModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Temperature(FrozenModel):
    comfort: Comfort
    water: Water
    air: Air


class Description(FrozenModel):
    full: str


class ModelItem(FrozenModel):
    precipitation: Precipitation
    pressure: Pressure
    humidity: Humidity
    icon: str
    gm: enums.GeomagneticField
    wind: Wind
    cloudiness: Cloudiness
    date: Date
    phenomenon: int | None = None
    radiation: Radiation
    city: int
    kind: enums.WeatherDataType
    storm: bool
    temperature: Temperature
    description: Description


Model: TypeAlias = tuple[ModelItem, ...]
