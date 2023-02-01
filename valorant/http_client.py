"""Client for API requests"""

from typing import Any

import requests

from .errors import NotFound


class Route:
    BASE_URL: str = "https://valorant-api.com/v1"

    def __init__(self, path: str):
        self.path: str = path
        self.url = self.BASE_URL + path


class HTTPClient:
    """HTTP Client for requesting data"""

    def __init__(self, lang: str) -> None:
        self.lang = lang

    def request(self, route: Route, **params) -> Any:
        """The method for requesting data"""

        params.update({"language": self.lang})

        url = route.url
        data = requests.get(url, params=params)

        if data.json()["status"] == 404:
            raise NotFound(data)

        return data.json()["data"]
