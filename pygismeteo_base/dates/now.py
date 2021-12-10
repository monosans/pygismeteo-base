# -*- coding: utf-8 -*-
from lxml.html import fromstring

from pygismeteo_base.dates.abc import ABCDate
from pygismeteo_base.utils import normalize_str


class Now(ABCDate):
    """Возвращается методом now() класса Gismeteo."""

    def __init__(self, html: bytes) -> None:
        self._tree = fromstring(html)

    @property
    def status(self) -> str:
        """Ясно, пасмурно, сильный дождь и т. д."""
        return self._build_result('//div[contains(@class,"now-desc")]/text()')

    @property
    def temperature(self) -> str:
        """Температура, °C."""
        return self._build_result(
            '//div[contains(@class,"now-weather")]'
            + '/span[contains(@class,"unit_temperature_c")]//text()'
        )

    @property
    def real_feel(self) -> str:
        """Температура по ощущению, °C."""
        return self._build_result(
            '//div[contains(@class,"now-feel")]'
            + '/*[contains(@class,"unit_temperature_c")]/text()'
        )

    @property
    def sunrise(self) -> str:
        """Заход."""
        return self._build_result(
            '//div[contains(@class,"now-astro-sunrise")]'
            + '/div[contains(@class,"time")]/text()'
        )

    @property
    def sunset(self) -> str:
        """Восход."""
        return self._build_result(
            '//div[contains(@class,"now-astro-sunset")]'
            + '/div[contains(@class,"time")]/text()'
        )

    @property
    def wind_speed(self) -> str:
        """Скорость ветра, м/с."""
        return self._build_result(
            '//div[contains(@class,"unit_wind_m_s")]/text()'
        )

    @property
    def wind_direction(self) -> str:
        """Направление ветра."""
        return self._build_result(
            '//div[contains(@class,"unit_wind_m_s")]'
            + '/div[contains(@class,"item-measure")]/div[last()]/text()'
        )

    @property
    def pressure(self) -> str:
        """Давление, мм рт. ст."""
        return self._build_result(
            '//div[contains(@class,"unit_pressure_mm_hg_atm")]/text()'
        )

    @property
    def humidity(self) -> str:
        """Влажность, %."""
        return self._build_result(
            '//div[contains(@class,"humidity")]'
            + '/div[contains(@class,"value")]/text()'
        )

    @property
    def gm_activity(self) -> str:
        """Геомагнитная активность, Кп-индекс."""
        return self._build_result(
            '//div[contains(@class,"gm")]'
            + '//div[contains(@class,"value")]/text()'
        )

    @property
    def water(self) -> str:
        """Температура воды, °C."""
        return self._build_result(
            '//div[contains(@class,"water")]'
            + '//div[contains(@class,"unit_temperature_c")]/text()'
        )

    def _build_result(self, xpath: str) -> str:
        return normalize_str(
            "".join(self._tree.xpath(f'//div[contains(@class,"now")]{xpath}'))
        )
