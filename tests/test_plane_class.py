import pytest
from opensky_api import StateVector

from src.plane_class import Aeroplane


def test_init(aeroplane):
    assert aeroplane.callsign == "ZOV"
    assert aeroplane.origin_country == "Russia"
    assert aeroplane.velocity == 10.5
    assert aeroplane.baro_altitude == 12


def test_init_callsign_ValueError():
    with pytest.raises(ValueError) as e:
        Aeroplane(None, None, None, None)
    assert str(e.value) == "Самолет должен содержать позывной"


def test_init_origin_country_ValueError():
    with pytest.raises(ValueError) as e:
        Aeroplane("Test", None, None, None)
    assert str(e.value) == "Самолет должен содержать страну происхождения"


def test_init_velocity_ValueError():
    with pytest.raises(ValueError) as e:
        Aeroplane("test", "test", -1, None)
    assert str(e.value) == "Скорость не должна быть меньше нуля"


def test_str(aeroplane):
    assert str(aeroplane) == "ZOV - Russia - 10.5 m/s - 12 m"


@pytest.mark.parametrize(
    "statevector, callsign, origin_country, velocity, baro_altitude",
    [
        (
            StateVector(
                [
                    "ab6fdd",
                    "AAL1667 ",
                    "United States",
                    1795522393,
                    1795522393,
                    -87.2008,
                    42.431,
                    2964.18,
                    False,
                    146.01,
                    249.59,
                    -5.53,
                    None,
                    3009.9,
                    "3016",
                    False,
                    0,
                    1,
                ]
            ),
            "AAL1667 ",
            "United States",
            146.01,
            2964.18,
        ),
        (
            StateVector(
                [
                    "3cf0b8",
                    "PTN62P  ",
                    "Germany",
                    1795522393,
                    1795522393,
                    -1.4925,
                    51.9483,
                    4937.76,
                    False,
                    158.29,
                    152.94,
                    18.53,
                    None,
                    4960.62,
                    "2272",
                    False,
                    0,
                    0,
                ]
            ),
            "PTN62P  ",
            "Germany",
            158.29,
            4937.76,
        ),
        (
            StateVector(
                [
                    "39de55",
                    "TVF967R ",
                    "France",
                    1795522393,
                    1795522393,
                    21.007,
                    46.0139,
                    11582.4,
                    False,
                    197.89,
                    305.8,
                    0,
                    None,
                    11391.9,
                    "1000",
                    False,
                    0,
                    0,
                ]
            ),
            "TVF967R ",
            "France",
            197.89,
            11582.4,
        ),
        (
            StateVector(
                [
                    "3d23f5",
                    "DELWF   ",
                    "Germany",
                    1795522393,
                    1795522393,
                    10.0631,
                    48.5134,
                    1226.82,
                    False,
                    48.15,
                    53.25,
                    0.65,
                    None,
                    1318.26,
                    "7000",
                    False,
                    0,
                    0,
                ]
            ),
            "DELWF   ",
            "Germany",
            48.15,
            1226.82,
        ),
        (
            StateVector(
                [
                    "39de48",
                    "TVF36CQ ",
                    "France",
                    1795522393,
                    1795522393,
                    1.3388,
                    44.4764,
                    11109.96,
                    False,
                    240.19,
                    356.44,
                    -2.93,
                    None,
                    11285.22,
                    "5571",
                    False,
                    0,
                    0,
                ]
            ),
            "TVF36CQ ",
            "France",
            240.19,
            11109.96,
        ),
    ],
)
def test_cast_to_object_list(
    statevector, callsign, origin_country, velocity, baro_altitude
):
    object_list = Aeroplane.cast_to_object_list([statevector])
    assert object_list[0].callsign == callsign
    assert object_list[0].origin_country == origin_country
    assert object_list[0].velocity == velocity
    assert object_list[0].baro_altitude == baro_altitude


def test_cast_to_object_list_error():
    with pytest.raises(ValueError) as e:
        Aeroplane.cast_to_object_list([1])
    assert str(e.value) == "Самолет должен принадлежать классу Statevector"


def test_review_by_baro_altitude(aeroplane1, aeroplane):
    assert aeroplane.review_by_baro_altitude(aeroplane1) == False


def test_review_by_baro_altitude_other_side(aeroplane1, aeroplane):
    assert aeroplane1.review_by_baro_altitude(aeroplane)


def test_review_by_baro_altitude_TypeError(aeroplane1):
    with pytest.raises(TypeError) as e:
        aeroplane1.review_by_baro_altitude(1)
    assert str(e.value) == "Второй объект не принадлежит классу aeroplane"


def test_review_by_baro_altitude_with_None(aeroplane_none, aeroplane):
    assert aeroplane.review_by_baro_altitude(aeroplane_none)


def test_review_by_baro_altitude_with_None_other_side(aeroplane_none, aeroplane):
    assert aeroplane_none.review_by_baro_altitude(aeroplane) == False


def test_review_by_velocity(aeroplane1, aeroplane):
    assert aeroplane.review_by_velocity(aeroplane1) == False


def test_review_by_velocity_other_side(aeroplane1, aeroplane):
    assert aeroplane1.review_by_velocity(aeroplane)


def test_review_by_velocity_TypeError(aeroplane1):
    with pytest.raises(TypeError) as e:
        aeroplane1.review_by_velocity(1)
    assert str(e.value) == "Второй объект не принадлежит классу aeroplane"


def test_review_by_velocity_with_None(aeroplane_none, aeroplane):
    assert aeroplane.review_by_velocity(aeroplane_none)


def test_review_by_velocity_with_None_other_side(aeroplane_none, aeroplane):
    assert aeroplane_none.review_by_velocity(aeroplane) == False
