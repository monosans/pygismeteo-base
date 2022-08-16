from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class Precipitation(BaseModel):
    type_ext: Optional[int] = Field(default=None)
    intensity: int
    correction: Optional[bool] = Field(default=None)
    amount: float
    duration: int
    type: int


class Pressure(BaseModel):
    h_pa: Optional[int] = Field(default=None)
    mm_hg_atm: Optional[int] = Field(default=None)
    in_hg: Optional[float] = Field(default=None)


class Humidity(BaseModel):
    percent: int


class Direction(BaseModel):
    degree: Optional[int] = Field(default=None)
    scale_8: Optional[int] = Field(default=None)


class Speed(BaseModel):
    km_h: int
    m_s: int
    mi_h: int


class Wind(BaseModel):
    direction: Direction
    speed: Speed


class Cloudiness(BaseModel):
    type: int
    percent: int


class Date(BaseModel):
    utc: str = Field(..., alias="UTC")
    time_zone_offset: int
    local: str
    hr_to_forecast: Optional[int] = Field(default=None)
    unix: int


class Radiation(BaseModel):
    uvb_index: int
    uvb: int = Field(..., alias="UVB")


class Comfort(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Water(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Air(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


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
    gm: int
    wind: Wind
    cloudiness: Cloudiness
    date: Date
    phenomenon: Optional[int] = Field(default=None)
    radiation: Radiation
    city: int
    kind: str
    storm: bool
    temperature: Temperature
    description: Description


class Model(BaseModel):
    __root__: List[ModelItem]
