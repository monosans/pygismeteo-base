from __future__ import annotations

from typing import Optional, Tuple

from pydantic import ConfigDict, Field, RootModel

from . import enums
from ._base import FrozenModel


class Precipitation(FrozenModel):
    type_ext: Optional[int] = None
    intensity: enums.PrecipitationIntensity
    correction: Optional[bool] = None
    amount: Optional[float] = None
    duration: int
    type: enums.PrecipitationType


class Pressure(FrozenModel):
    h_pa: int
    mm_hg_atm: int
    in_hg: float


class Humidity(FrozenModel):
    percent: Optional[int] = None


class Direction(FrozenModel):
    degree: Optional[int] = None
    scale_8: Optional[enums.WindScale8] = None


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
    hr_to_forecast: Optional[int] = None
    unix: int


class Radiation(FrozenModel):
    uvb_index: Optional[int] = None
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
    phenomenon: Optional[int] = None
    radiation: Radiation
    city: int
    kind: enums.WeatherDataType
    storm: bool
    temperature: Temperature
    description: Description


class Model(RootModel[Tuple[ModelItem, ...]]):
    model_config = ConfigDict(frozen=True)


class Response(FrozenModel):
    response: Model
