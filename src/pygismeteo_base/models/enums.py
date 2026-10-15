"""Перечисления с описанием значений на русском и английском.

Члены записаны как `(значение, описание на английском, описание на русском)`.
Например, `PrecipitationType.RAIN` равен `1`, а его `description.ru`
равно `"Дождь"`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Final

from pygismeteo_base._enum import IntEnum, StrEnum


@dataclass(frozen=True)
class Description:
    """Описание значения."""

    __slots__ = ("en", "ru")

    en: str
    """На английском."""
    ru: str
    """На русском."""


class _DescriptionMixin:
    if TYPE_CHECKING:
        description: Description
    else:

        def __init__(
            self, _: Any, description_en: str, description_ru: str, /
        ) -> None:
            self.description: Final = Description(
                en=description_en, ru=description_ru
            )


class IntEnumWithDescription(_DescriptionMixin, IntEnum):
    """Целочисленное перечисление с описанием значений."""


class StrEnumWithDescription(_DescriptionMixin, StrEnum):
    """Строковое перечисление с описанием значений."""


class WeatherDataType(StrEnumWithDescription):
    """Тип данных: наблюдение или прогноз."""

    OBS = "Obs", "Observation", "Наблюдение"
    FRC = "Frc", "Forecast", "Прогноз"


class CloudinessType(IntEnumWithDescription):
    """Облачность."""

    SUNNY = 0, "Sunny", "Ясно"
    MOSTLY_SUNNY = 1, "Mostly sunny", "Малооблачно"
    MOSTLY_CLOUDY = 2, "Mostly cloudy", "Облачно"
    OVERCAST = 3, "Overcast", "Пасмурно"
    PARTLY_CLOUDY = 101, "Partly cloudy", "Переменная облачность"


class PrecipitationType(IntEnumWithDescription):
    """Тип осадков."""

    NO_PRECIPITATION = 0, "No precipitation", "Нет осадков"
    RAIN = 1, "Rain", "Дождь"
    SNOW = 2, "Snow", "Снег"
    MIXED_PRECIPITATION = 3, "Mixed precipitation", "Смешанные осадки"


class PrecipitationIntensity(IntEnumWithDescription):
    """Интенсивность осадков."""

    NO_PRECIPITATION = 0, "No precipitation", "Нет осадков"
    RAIN = 1, "Light rain / snow", "Небольшой дождь / снег"
    SNOW = 2, "Rain / snow", "Дождь / снег"
    MIXED_PRECIPITATION = 3, "Heavy rain / snow", "Сильный дождь / снег"


class GeomagneticField(IntEnumWithDescription):
    """Геомагнитная обстановка, от 1 до 8 баллов."""

    NO_SIGNIFICANT_DISTURBANCES = (
        1,
        "No significant disturbances",
        "Нет заметных возмущений",
    )
    SMALL_DISTURBANCES = 2, "Small disturbances", "Небольшие возмущения"
    WEAK_GEOMAGNETIC_STORM = (
        3,
        "Weak geomagnetic storm",
        "Слабая геомагнитная буря",
    )
    MINOR_GEOMAGNETIC_STORM = (
        4,
        "Minor geomagnetic storm",
        "Малая геомагнитная буря",
    )
    MODERATE_GEOMAGNETIC_STORM = (
        5,
        "Moderate geomagnetic storm",
        "Умеренная геомагнитная буря",
    )
    STRONG_GEOMAGNETIC_STORM = (
        6,
        "Strong geomagnetic storm",
        "Сильная геомагнитная буря",
    )
    SEVERE_GEOMAGNETIC_STORM = (
        7,
        "Severe geomagnetic storm",
        "Жесткий геомагнитный шторм",
    )
    EXTREME_GEOMAGNETIC_STORM = (
        8,
        "Extreme geomagnetic storm",
        "Экстремальный шторм",
    )


class WindScale8(IntEnumWithDescription):
    """Направление ветра по 8 румбам, 0 означает штиль."""

    CALM = 0, "Calm", "Штиль"
    NORTHERLY = 1, "Northerly", "Северный"
    NORTHEASTERLY = 2, "Northeasterly", "Северо-восточный"
    EASTERLY = 3, "Easterly", "Восточный"
    SOUTHEASTERLY = 4, "Southeasterly", "Юго-восточный"
    SOUTHERLY = 5, "Southerly", "Южный"
    SOUTHWESTERLY = 6, "Southwesterly", "Юго-западный"
    WESTERLY = 7, "Westerly", "Западный"
    NORTHWESTERLY = 8, "Northwesterly", "Северо-западный"


class GeographicObjectType(StrEnumWithDescription):
    """Тип географического объекта."""

    CITY = "T", "City", "Город"
    METROPOLIS = "C", "Metropolis", "Метрополис"
    AIRPORT = "A", "Airport", "Аэропорт"
    WEATHER_STATION = "M", "Weather station", "Метеостанция"
