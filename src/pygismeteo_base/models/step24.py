"""Прогноз с шагом 24 часа. Запрос возвращает `Model`."""

from __future__ import annotations

from typing import TypeAlias

from pydantic import Field

from pygismeteo_base.models import enums
from pygismeteo_base.models._base import FrozenModel


class Precipitation(FrozenModel):
    """Осадки."""

    type_ext: int | None = None
    intensity: enums.PrecipitationIntensity
    amount: float
    """Количество осадков, мм."""
    type: enums.PrecipitationType


class HPa(FrozenModel):
    """Давление в гПа: минимум и максимум."""

    max: int
    min: int


class MmHgAtm(FrozenModel):
    """Давление в мм рт. ст.: минимум и максимум."""

    max: int
    min: int


class InHg(FrozenModel):
    """Давление в дюймах рт. ст.: минимум и максимум."""

    max: float
    min: float


class Pressure(FrozenModel):
    """Атмосферное давление."""

    h_pa: HPa
    mm_hg_atm: MmHgAtm
    in_hg: InHg


class Percent(FrozenModel):
    """Влажность в процентах: минимум, максимум и среднее."""

    max: int
    min: int
    avg: int


class Humidity(FrozenModel):
    """Относительная влажность."""

    percent: Percent


class Description(FrozenModel):
    """Текстовое описание погоды."""

    full: str


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
    unix: int
    """Unix-время, в секундах."""


class Radiation(FrozenModel):
    """Ультрафиолетовое излучение."""

    max: int | None = None
    max_index: int | None = None


class Max(FrozenModel):
    """Максимум."""

    c: float = Field(alias="C")
    """В °C."""
    f: float = Field(alias="F")
    """В °F."""


class Min(FrozenModel):
    """Минимум."""

    c: float = Field(alias="C")
    """В °C."""
    f: float = Field(alias="F")
    """В °F."""


class Comfort(FrozenModel):
    """Температура по ощущению."""

    max: Max
    min: Min


class Max1(FrozenModel):
    """Максимум."""

    c: float | None = Field(default=None, alias="C")
    """В °C."""
    f: float | None = Field(default=None, alias="F")
    """В °F."""


Min1 = Min


class Water(FrozenModel):
    """Температура воды."""

    max: Max1
    min: Min


class Max2(FrozenModel):
    """Максимум."""

    c: float = Field(alias="C")
    """В °C."""
    f: float = Field(alias="F")
    """В °F."""


Min2 = Min


class Avg(FrozenModel):
    """Среднее."""

    c: float = Field(alias="C")
    """В °C."""
    f: float = Field(alias="F")
    """В °F."""


class Air(FrozenModel):
    """Температура воздуха."""

    max: Max2
    min: Min
    avg: Avg


class Temperature(FrozenModel):
    """Температура."""

    comfort: Comfort
    water: Water
    air: Air


class Max3(FrozenModel):
    """Максимум."""

    km_h: int
    """В км/ч."""
    m_s: int
    """В м/с."""
    mi_h: int
    """В милях в час."""


class Min3(FrozenModel):
    """Минимум."""

    km_h: int
    """В км/ч."""
    m_s: int
    """В м/с."""
    mi_h: int
    """В милях в час."""


class Avg1(FrozenModel):
    """Среднее."""

    km_h: int | None = None
    """В км/ч."""
    m_s: int | None = None
    """В м/с."""
    mi_h: int | None = None
    """В милях в час."""


class Speed(FrozenModel):
    """Скорость ветра."""

    max: Max3
    min: Min3
    avg: Avg1


class Max4(FrozenModel):
    """Максимум."""

    degree: int | None = None
    """В градусах."""
    scale_8: enums.WindScale8 | None = None
    """По 8 румбам."""


class Min4(FrozenModel):
    """Минимум."""

    degree: int | None = None
    """В градусах."""
    scale_8: enums.WindScale8 | None = None
    """По 8 румбам."""


class Avg2(FrozenModel):
    """Среднее."""

    degree: int | None = None
    """В градусах."""
    scale_8: enums.WindScale8 | None = None
    """По 8 румбам."""


class Direction(FrozenModel):
    """Направление ветра."""

    max: Max4
    min: Min4
    avg: Avg2


class Wind(FrozenModel):
    """Ветер."""

    speed: Speed
    direction: Direction


class ModelItem(FrozenModel):
    """Прогноз на одни сутки."""

    precipitation: Precipitation
    pressure: Pressure
    humidity: Humidity
    gm: enums.GeomagneticField
    """Геомагнитная обстановка."""
    description: Description
    cloudiness: Cloudiness
    date: Date
    phenomenon: int | None = None
    radiation: Radiation
    city: int
    """ID географического объекта."""
    kind: enums.WeatherDataType | None = None
    """Наблюдение или прогноз."""
    storm: bool
    temperature: Temperature
    wind: Wind
    icon: str
    """Код значка погоды."""


Model: TypeAlias = tuple[ModelItem, ...]
"""Прогноз: по элементу на сутки."""
