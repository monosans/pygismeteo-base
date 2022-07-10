from __future__ import annotations

from pydantic import BaseModel, Field


class Precipitation(BaseModel):
    type_ext: int | None
    intensity: int
    correction: bool | None
    amount: float
    duration: int
    type: int


class Pressure(BaseModel):
    h_pa: int | None
    mm_hg_atm: int | None
    in_hg: float | None


class Humidity(BaseModel):
    percent: int


class Direction(BaseModel):
    degree: int | None
    scale_8: int | None


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
    hr_to_forecast: int | None
    unix: int


class Radiation(BaseModel):
    uvb_index: int | None
    uvb: int | None = Field(..., alias="UVB")


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
    phenomenon: int | None
    radiation: Radiation
    city: int
    kind: str
    storm: bool
    temperature: Temperature
    description: Description


class Model(BaseModel):
    __root__: list[ModelItem]
