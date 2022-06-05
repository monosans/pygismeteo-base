from pygismeteo_base import types, validators


class Search:
    __slots__ = ()

    @staticmethod
    def _get_params_by_coordinates(
        latitude: float, longitude: float, *, limit: types.SearchLimit
    ) -> types.Params:
        coordinates = validators.Coordinates(
            latitude=latitude, longitude=longitude
        )
        params = coordinates.dict()
        if limit is not None:
            lim = validators.SearchLimit.parse_obj(limit).__root__
            params.update({"limit": lim})
        return params

    @staticmethod
    def _get_params_by_ip(ip: str) -> types.Params:
        ip = str(validators.IPAddress.parse_obj(ip).__root__)
        return {"ip": ip}

    @staticmethod
    def _get_params_by_query(query: str) -> types.Params:
        query = validators.Query.parse_obj(query).__root__
        return {"query": query}

    @property
    def _endpoint(self) -> str:
        return "search/cities"
