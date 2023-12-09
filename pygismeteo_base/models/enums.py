from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from typing_extensions import Any

from ._enum import IntEnum, StrEnum


@dataclass(frozen=True)
class Description:
    __slots__ = ("en", "ru")

    en: str
    ru: str


class _DescriptionMixin:
    if TYPE_CHECKING:
        description: Description
    else:

        def __init__(
            self, _: Any, description_en: str, description_ru: str, /
        ) -> None:
            self.description = Description(en=description_en, ru=description_ru)


class IntEnumWithDescription(_DescriptionMixin, IntEnum):
    pass


class StrEnumWithDescription(_DescriptionMixin, StrEnum):
    pass


class WeatherDataType(StrEnumWithDescription):
    OBS = "Obs", "Observation", "Наблюдение"
    FRC = "Frc", "Forecast", "Прогноз"


class CloudinessType(IntEnumWithDescription):
    SUNNY = 0, "Sunny", "Ясно"
    MOSTLY_SUNNY = 1, "Mostly sunny", "Малооблачно"
    MOSTLY_CLOUDY = 2, "Mostly cloudy", "Облачно"
    OVERCAST = 3, "Overcast", "Пасмурно"
    PARTLY_CLOUDY = 101, "Partly cloudy", "Переменная облачность"


class PrecipitationType(IntEnumWithDescription):
    NO_PRECIPITATION = 0, "No precipitation", "Нет осадков"
    RAIN = 1, "Rain", "Дождь"
    SNOW = 2, "Snow", "Снег"
    MIXED_PRECIPITATION = 3, "Mixed precipitation", "Смешанные осадки"


class PrecipitationIntensity(IntEnumWithDescription):
    NO_PRECIPITATION = 0, "No precipitation", "Нет осадков"
    RAIN = 1, "Light rain / snow", "Небольшой дождь / снег"
    SNOW = 2, "Rain / snow", "Дождь / снег"
    MIXED_PRECIPITATION = 3, "Heavy rain / snow", "Сильный дождь / снег"


class GeomagneticField(IntEnumWithDescription):
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
    CITY = "T", "City", "Город"
    METROPOLIS = "C", "Metropolis", "Метрополис"
    AIRPORT = "A", "Airport", "Аэропорт"
    WEATHER_STATION = "M", "Weather station", "Метеостанция"
