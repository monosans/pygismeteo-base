from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field, RootModel

from . import enums


class Precipitation(BaseModel):
    type_ext: Optional[int] = None
    intensity: enums.PrecipitationIntensity
    correction: Optional[bool] = None
    amount: Optional[float] = None
    duration: int
    type: enums.PrecipitationType


class Pressure(BaseModel):
    h_pa: int
    mm_hg_atm: int
    in_hg: float


class Humidity(BaseModel):
    percent: Optional[int] = None


class Direction(BaseModel):
    degree: Optional[int] = None
    scale_8: Optional[enums.WindScale8] = None


class Speed(BaseModel):
    km_h: int
    m_s: int
    mi_h: int


class Wind(BaseModel):
    direction: Direction
    speed: Speed


class Cloudiness(BaseModel):
    type: enums.CloudinessType
    percent: int


class Date(BaseModel):
    utc: str = Field(alias="UTC")
    time_zone_offset: int
    local: str
    hr_to_forecast: Optional[int] = None
    unix: int


class Radiation(BaseModel):
    uvb_index: Optional[int] = None
    uvb: int = Field(alias="UVB")


class Comfort(BaseModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Water(BaseModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Air(BaseModel):
    c: float = Field(alias="C")
    f: float = Field(alias="F")


class Temperature(BaseModel):
    comfort: Comfort
    water: Water
    air: Air


class Description(BaseModel):
    full: str


class ModelItem(BaseModel):
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


Model = RootModel[List[ModelItem]]


class Response(BaseModel):
    response: Model
