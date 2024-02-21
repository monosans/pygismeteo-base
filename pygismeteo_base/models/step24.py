from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, RootModel

from . import enums


class Precipitation(BaseModel):
    type_ext: Optional[int] = None
    intensity: enums.PrecipitationIntensity
    amount: float
    type: enums.PrecipitationType


class HPa(BaseModel):
    max: int
    min: int


class MmHgAtm(BaseModel):
    max: int
    min: int


class InHg(BaseModel):
    max: float
    min: float


class Pressure(BaseModel):
    h_pa: HPa
    mm_hg_atm: MmHgAtm
    in_hg: InHg


class Percent(BaseModel):
    max: int
    min: int
    avg: int


class Humidity(BaseModel):
    percent: Percent


class Description(BaseModel):
    full: str


class Cloudiness(BaseModel):
    type: enums.CloudinessType
    percent: int


class Date(BaseModel):
    utc: str = Field(alias="UTC")
    local: str
    time_zone_offset: int
    unix: int


class Radiation(BaseModel):
    max: Optional[int] = None
    max_index: Optional[int] = None


class Max(BaseModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Min(BaseModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Comfort(BaseModel):
    max: Max
    min: Min


class Max1(BaseModel):
    c: Optional[float] = Field(default=None, alias="C")
    f: Optional[float] = Field(default=None, alias="F")


Min1 = Min


class Water(BaseModel):
    max: Max1
    min: Min


class Max2(BaseModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


Min2 = Min


class Avg(BaseModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Air(BaseModel):
    max: Max2
    min: Min
    avg: Avg


class Temperature(BaseModel):
    comfort: Comfort
    water: Water
    air: Air


class Max3(BaseModel):
    km_h: int
    m_s: int
    mi_h: int


class Min3(BaseModel):
    km_h: int
    m_s: int
    mi_h: int


class Avg1(BaseModel):
    km_h: Optional[int] = None
    m_s: Optional[int] = None
    mi_h: Optional[int] = None


class Speed(BaseModel):
    max: Max3
    min: Min3
    avg: Avg1


class Max4(BaseModel):
    degree: Optional[int] = None
    scale_8: Optional[enums.WindScale8] = None


class Min4(BaseModel):
    degree: Optional[int] = None
    scale_8: Optional[enums.WindScale8] = None


class Avg2(BaseModel):
    degree: Optional[int] = None
    scale_8: Optional[enums.WindScale8] = None


class Direction(BaseModel):
    max: Max4
    min: Min4
    avg: Avg2


class Wind(BaseModel):
    speed: Speed
    direction: Direction


class ModelItem(BaseModel):
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


Model = RootModel[List[ModelItem]]


class Response(BaseModel):
    response: Model
