import json
import pathlib
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_aeroplane(self, aeroplane):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def get_top(self, num):
        pass


class JSONSaver(Saver):
    def __init__(
        self,
        file_path=str(
            pathlib.Path(pathlib.Path(__file__).resolve().parents[1])
            / "data"
            / "planes.json"
        ),
    ):
        if pathlib.Path.is_file(pathlib.Path(file_path)) == False:
            raise FileNotFoundError(f"Файл {file_path} не найден")
        self.file_path = file_path

    def load(self):
        try:
            with open(self.file_path, "r") as json_file:
                data = json.load(json_file)
            return data
        except Exception:
            return []

    def add_aeroplane(self, aeroplane):
        planes = self.load()
        print(planes)
        with open(self.file_path, "w") as json_file:
            planes.append(
                {
                    "callsign": aeroplane.callsign,
                    "origin_country": aeroplane.origin_country,
                    "velocity": aeroplane.velocity,
                    "baro_altitude": aeroplane.baro_altitude,
                }
            )
            json.dump(planes, json_file, indent=4)
            return planes

    def delete_aeroplane(self, aeroplane):
        planes = self.load()
        with open(self.file_path, "w") as json_file:
            try:
                planes.remove(
                    {
                        "callsign": aeroplane.callsign,
                        "origin_country": aeroplane.origin_country,
                        "velocity": aeroplane.velocity,
                        "baro_altitude": aeroplane.baro_altitude,
                    }
                )
                return planes
            except ValueError:
                raise ValueError("Самолета нет в файле")
            finally:
                json.dump(planes, json_file, indent=4)

    def get_top(self, num):
        if num < 1:
            raise ValueError("Количество должно быть больше нуля")
        planes = self.load()
        return planes[:num]
