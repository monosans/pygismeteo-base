from __future__ import annotations

from typing import Optional, Tuple

from pydantic import ConfigDict, Field, RootModel

from . import enums
from ._base import FrozenModel


class Precipitation(FrozenModel):
    type_ext: Optional[int] = None
    intensity: enums.PrecipitationIntensity
    amount: float
    type: enums.PrecipitationType


class HPa(FrozenModel):
    max: int
    min: int


class MmHgAtm(FrozenModel):
    max: int
    min: int


class InHg(FrozenModel):
    max: float
    min: float


class Pressure(FrozenModel):
    h_pa: HPa
    mm_hg_atm: MmHgAtm
    in_hg: InHg


class Percent(FrozenModel):
    max: int
    min: int
    avg: int


class Humidity(FrozenModel):
    percent: Percent


class Description(FrozenModel):
    full: str


class Cloudiness(FrozenModel):
    type: enums.CloudinessType
    percent: int


class Date(FrozenModel):
    utc: str = Field(alias="UTC")
    local: str
    time_zone_offset: int
    unix: int


class Radiation(FrozenModel):
    max: Optional[int] = None
    max_index: Optional[int] = None


class Max(FrozenModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Min(FrozenModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Comfort(FrozenModel):
    max: Max
    min: Min


class Max1(FrozenModel):
    c: Optional[float] = Field(default=None, alias="C")
    f: Optional[float] = Field(default=None, alias="F")


Min1 = Min


class Water(FrozenModel):
    max: Max1
    min: Min


class Max2(FrozenModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


Min2 = Min


class Avg(FrozenModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Air(FrozenModel):
    max: Max2
    min: Min
    avg: Avg


class Temperature(FrozenModel):
    comfort: Comfort
    water: Water
    air: Air


class Max3(FrozenModel):
    km_h: int
    m_s: int
    mi_h: int


class Min3(FrozenModel):
    km_h: int
    m_s: int
    mi_h: int


class Avg1(FrozenModel):
    km_h: Optional[int] = None
    m_s: Optional[int] = None
    mi_h: Optional[int] = None


class Speed(FrozenModel):
    max: Max3
    min: Min3
    avg: Avg1


class Max4(FrozenModel):
    degree: Optional[int] = None
    scale_8: Optional[enums.WindScale8] = None


class Min4(FrozenModel):
    degree: Optional[int] = None
    scale_8: Optional[enums.WindScale8] = None


class Avg2(FrozenModel):
    degree: Optional[int] = None
    scale_8: Optional[enums.WindScale8] = None


class Direction(FrozenModel):
    max: Max4
    min: Min4
    avg: Avg2


class Wind(FrozenModel):
    speed: Speed
    direction: Direction


class ModelItem(FrozenModel):
    precipitation: Precipitation
    pressure: Pressure
    humidity: Humidity
    gm: enums.GeomagneticField
    description: Description
    cloudiness: Cloudiness
    date: Date
    phenomenon: Optional[int] = None
    radiation: Radiation
    city: int
    kind: Optional[enums.WeatherDataType] = None
    storm: bool
    temperature: Temperature
    wind: Wind
    icon: str


class Model(RootModel[Tuple[ModelItem, ...]]):
    model_config = ConfigDict(frozen=True)


class Response(FrozenModel):
    response: Model
