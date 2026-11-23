import requests
cords = requests.get(
            url="https://nominatim.openstreetmap.org/search",
            params={"q": "Russia", "format": "geojson"},
            headers={"user-agent": "Plane_tracker"},
            timeout=10,
        )
print(cords.json()["features"][0]["geometry"]["coordinates"])