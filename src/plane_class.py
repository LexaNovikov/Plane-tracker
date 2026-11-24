from opensky_api import StateVector


class Aeroplane:
    def __init__(self, callsign, origin_country, velocity, baro_altitude):
        if callsign is None:
            raise ValueError("Самолет должен содержать позывной")
        if origin_country is None:
            raise ValueError("Самолет должен содержать страну происхождения")
        if velocity is not None and velocity < 0:
            raise ValueError("Скорость не должна быть меньше нуля")
        self.callsign = callsign
        self.origin_country = origin_country
        self.velocity = velocity
        self.baro_altitude = baro_altitude

    def __str__(self):
        return f"{self.callsign} - {self.origin_country} - {self.velocity} m/s - {self.baro_altitude} m"

    @classmethod
    def cast_to_object_list(cls, aeroplanes):
        filtered_aeroplanes = []
        for aeroplane in aeroplanes:
            if type(aeroplane) != StateVector:
                raise ValueError("Самолет должен принадлежать классу Statevector")
            filtered_aeroplanes.append(
                Aeroplane(
                    aeroplane.callsign,
                    aeroplane.origin_country,
                    aeroplane.velocity,
                    aeroplane.baro_altitude,
                )
            )
        return filtered_aeroplanes

    def review_by_baro_altitude(self, other_aeroplane):
        if not isinstance(other_aeroplane, Aeroplane):
            raise TypeError("Второй объект не принадлежит классу aeroplane")
        if self.baro_altitude is None:
            return False
        if other_aeroplane.baro_altitude is None:
            return True
        if self.baro_altitude > other_aeroplane.baro_altitude:
            return True
        return False

    def review_by_velocity(self, other_aeroplane):
        if not isinstance(other_aeroplane, Aeroplane):
            raise TypeError("Второй объект не принадлежит классу aeroplane")
        if self.velocity is None:
            return False
        if other_aeroplane.velocity is None:
            return True
        if self.velocity > other_aeroplane.velocity:
            return True
        return False
