from opensky_api import StateVector

from src.connect_class import Connect
class Aircraft:
    def __init__(self, aircraft):
        if not isinstance(aircraft, StateVector):
            raise TypeError("Объект не является экземпляром класса StateVector")
        self.aircraft = aircraft
        self.name = self.aircraft.callsign
        self.origin_country = self.aircraft.origin_country
        self.velocity = self.aircraft.velocity
        self.baro_altitude = self.aircraft.baro_altitude
    def review_by_baro_altitude(self, other_aircraft):
        if not isinstance(other_aircraft, Aircraft):
            raise TypeError("Второй объект не принадлежит классу Aircraft")
        if self.baro_altitude is None or other_aircraft.baro_altitude is None:
            raise ValueError("У одного из самолетов неизвестная высота")
        if self.baro_altitude > other_aircraft.baro_altitude:
            return self.aircraft
        return other_aircraft
    def review_by_velocity(self, other_aircraft):
        if not isinstance(other_aircraft, Aircraft):
            raise TypeError("Второй объект не принадлежит классу Aircraft")
        if self.velocity is None or other_aircraft.velocity is None:
            raise ValueError("У одного из самолетов неизвестная скорость")
        if self.velocity > other_aircraft.velocity:
            return self.aircraft
        return other_aircraft
c = Connect("Russia")
print(*c.get_planes_info(), sep="\n")
plane = Aircraft(c.get_planes_info()[-1])
plane1 = Aircraft(c.get_planes_info()[-2])
print(plane.review_by_baro_altitude(plane1))
print(plane.review_by_velocity(plane1))
