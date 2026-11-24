import pathlib
from abc import ABC, abstractmethod

import requests
from opensky_api import OpenSkyApi, TokenManager


class AbcAeroplanesAPI(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_country_cords(self):
        pass

    @abstractmethod
    def get_aeroplanes(self):
        pass


class AeroplanesAPI(AbcAeroplanesAPI):
    def __init__(self, country_name):
        self.country_name = country_name

    def get_country_cords(self):
        cords = requests.get(
            url="https://nominatim.openstreetmap.org/search",
            params={"q": self.country_name, "format": "geojson"},
            headers={"user-agent": "Plane_tracker"},
            timeout=10,
        )
        west, south, east, north = cords.json()["features"][0]["bbox"]
        return (south, north, west, east)

    def get_aeroplanes(self):
        base_dir = pathlib.Path(__file__).resolve().parents[1]
        api = OpenSkyApi(
            token_manager=TokenManager.from_json_file(
                str(base_dir / "data" / "credentials.json")
            )
        )
        return api.get_states(bbox=self.get_country_cords()).states
