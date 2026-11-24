import pytest
from opensky_api import StateVector

from src.connect_class import AeroplanesAPI
from src.plane_class import Aeroplane
from src.saver_class import JSONSaver


@pytest.fixture
def aeroplane():
    return Aeroplane("ZOV", "Russia", 10.5, 12)


@pytest.fixture
def aeroplane_none():
    return Aeroplane("ZOV", "Russia", None, None)


@pytest.fixture
def aeroplane1():
    return Aeroplane("ZOV", "Russia", 101.5, 121)


@pytest.fixture
def aeroplanes():
    return [
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
    ]


@pytest.fixture
def API():
    return AeroplanesAPI("Russia")


@pytest.fixture
def Json_saver():
    return JSONSaver()
