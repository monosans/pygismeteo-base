from typing import List, Optional

from pydantic import BaseModel, Field


class Precipitation(BaseModel):
    type_ext: Optional[int]
    intensity: int
    amount: float
    type: int


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
    type: int
    percent: int


class Date(BaseModel):
    utc: str = Field(..., alias="UTC")
    local: str
    time_zone_offset: int
    unix: int


class Radiation(BaseModel):
    max: Optional[int]
    max_index: Optional[int]


class Max(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Min(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Comfort(BaseModel):
    max: Max
    min: Min


class Max1(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Min1(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Water(BaseModel):
    max: Max1
    min: Min1


class Max2(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Min2(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Avg(BaseModel):
    c: float = Field(..., alias="C")
    f: float = Field(..., alias="F")


class Air(BaseModel):
    max: Max2
    min: Min2
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
    km_h: Optional[int]
    m_s: Optional[int]
    mi_h: Optional[int]


class Speed(BaseModel):
    max: Max3
    min: Min3
    avg: Avg1


class Max4(BaseModel):
    degree: Optional[int]
    scale_8: Optional[int]


class Min4(BaseModel):
    degree: Optional[int]
    scale_8: Optional[int]


class Avg2(BaseModel):
    degree: Optional[int]
    scale_8: Optional[int]


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
    gm: int
    description: Description
    cloudiness: Cloudiness
    date: Date
    phenomenon: Optional[int]
    radiation: Radiation
    city: int
    kind: Optional[str]
    storm: bool
    temperature: Temperature
    wind: Wind
    icon: str


class Model(BaseModel):
    __root__: List[ModelItem]
