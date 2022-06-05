from typing import List, Optional

from pydantic import BaseModel, Field


class Precipitation(BaseModel):
    type_ext: Optional[int]
    intensity: int
    correction: Optional[bool]
    amount: Optional[float]
    duration: int
    type: int


class Pressure(BaseModel):
    h_pa: int
    mm_hg_atm: int
    in_hg: float


class Humidity(BaseModel):
    percent: Optional[int]


class Direction(BaseModel):
    degree: Optional[int]
    scale_8: Optional[int]


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
    hr_to_forecast: Optional[int]
    unix: int


class Radiation(BaseModel):
    uvb_index: Optional[int]
    uvb: Optional[int] = Field(..., alias="UVB")


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
    phenomenon: Optional[int]
    radiation: Radiation
    city: int
    kind: str
    storm: bool
    temperature: Temperature
    description: Description


class Model(BaseModel):
    __root__: List[ModelItem]
