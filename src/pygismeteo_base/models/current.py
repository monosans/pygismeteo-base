"""Текущая погода. Ответ имеет тип `Model`."""

from __future__ import annotations

from pydantic import Field

from pygismeteo_base.models import enums
from pygismeteo_base.models._base import FrozenModel


class Precipitation(FrozenModel):
    """Осадки."""

    type_ext: int | None = None
    intensity: enums.PrecipitationIntensity
    correction: bool | None = None
    amount: float | None = None
    """Количество осадков, мм."""
    duration: int
    type: enums.PrecipitationType


class Pressure(FrozenModel):
    """Атмосферное давление."""

    h_pa: int | None = None
    """В гПа."""
    mm_hg_atm: int | None = None
    """В мм рт. ст."""
    in_hg: float | None = None
    """В дюймах рт. ст."""


class Humidity(FrozenModel):
    """Относительная влажность."""

    percent: int | None = None
    """В процентах."""


class Direction(FrozenModel):
    """Направление ветра."""

    degree: int | None = None
    """В градусах."""
    scale_8: enums.WindScale8 | None = None
    """По 8 румбам."""


class Speed(FrozenModel):
    """Скорость ветра."""

    km_h: int
    """В км/ч."""
    m_s: int
    """В м/с."""
    mi_h: int
    """В милях в час."""


class Wind(FrozenModel):
    """Ветер."""

    direction: Direction
    speed: Speed


class Cloudiness(FrozenModel):
    """Облачность."""

    type: enums.CloudinessType
    percent: int
    """В процентах."""


class Date(FrozenModel):
    """Дата и время."""

    utc: str = Field(alias="UTC")
    """Время UTC."""
    local: str
    """Местное время."""
    time_zone_offset: int
    """Смещение местного времени от UTC, в минутах."""
    hr_to_forecast: int | None = None
    unix: int
    """Unix-время, в секундах."""


class Radiation(FrozenModel):
    """Ультрафиолетовое излучение."""

    uvb_index: int | None = None
    uvb: int | None = Field(default=None, alias="UVB")


class Comfort(FrozenModel):
    """Температура по ощущению."""

    c: float = Field(alias="C")
    """В °C."""
    f: float = Field(alias="F")
    """В °F."""


class Water(FrozenModel):
    """Температура воды."""

    c: float = Field(alias="C")
    """В °C."""
    f: float = Field(alias="F")
    """В °F."""


class Air(FrozenModel):
    """Температура воздуха."""

    c: float = Field(alias="C")
    """В °C."""
    f: float = Field(alias="F")
    """В °F."""


class Temperature(FrozenModel):
    """Температура."""

    comfort: Comfort
    water: Water
    air: Air


class Description(FrozenModel):
    """Текстовое описание погоды."""

    full: str


class Model(FrozenModel):
    """Текущая погода."""

    precipitation: Precipitation
    pressure: Pressure
    humidity: Humidity
    icon: str
    """Код значка погоды."""
    gm: enums.GeomagneticField
    """Геомагнитная обстановка."""
    wind: Wind
    cloudiness: Cloudiness
    date: Date
    phenomenon: int | None = None
    radiation: Radiation
    city: int
    """ID географического объекта."""
    kind: enums.WeatherDataType
    """Наблюдение или прогноз."""
    storm: bool
    temperature: Temperature
    description: Description
