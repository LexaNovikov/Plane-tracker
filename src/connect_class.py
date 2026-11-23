from abc import ABC, abstractmethod
import pathlib
import requests
from opensky_api import OpenSkyApi, TokenManager, StateVector

# import requests
# response = requests.get(
#     "https://nominatim.openstreetmap.org/search",
#     params={"q": "Russia", "format": "geojson"},
#     headers={"User-Agent": "PlaneTracker/0.1 (contact: lexaproxa228@gmail.com)"},
#     timeout=10,
# )
# print(response.status_code, response.text)

class AbcConnect(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def get_cords(self):
        pass
    @abstractmethod
    def get_planes_info(self):
        pass

class Connect(AbcConnect):
    def __init__(self, country_name):
        self.country_name = country_name
    def get_cords(self):
        cords = requests.get(
            url="https://nominatim.openstreetmap.org/search",
            params={"q": self.country_name, "format": "geojson"},
            headers={"user-agent": "Plane_tracker"},
            timeout=10,
        )
        west, south, east, north = cords.json()["features"][0]["bbox"]
        return south, north, west, east

    def get_planes_info(self):
        base_dir = pathlib.Path(__file__).resolve().parents[1]
        api = OpenSkyApi(token_manager=TokenManager.from_json_file(str(base_dir / "data" / "credentials.json")))
        s = api.get_states(bbox=self.get_cords())

        return s.states

