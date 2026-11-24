import pathlib
from unittest.mock import patch

import pytest

from src.saver_class import JSONSaver


def test_init(Json_saver):
    assert Json_saver.file_path == str(
        pathlib.Path(__file__).resolve().parents[1] / "data" / "planes.json"
    )


def test_init_error():
    with pytest.raises(FileNotFoundError) as e:
        JSONSaver("sdf")
    assert str(e.value) == "Файл sdf не найден"


@patch("json.load")
def test_load(mock_load, Json_saver):
    mock_load.return_value = {"planes": [{"test"}]}
    assert Json_saver.load() == {"planes": [{"test"}]}


@patch("json.dump")
@patch("json.load")
def test_add_aeroplane(mock_load, mock_dump, Json_saver, aeroplane1):
    mock_load.return_value = [{"test"}]
    mock_dump.return_value = None
    assert Json_saver.add_aeroplane(aeroplane1) == [
        {"test"},
        {
            "callsign": aeroplane1.callsign,
            "origin_country": aeroplane1.origin_country,
            "velocity": aeroplane1.velocity,
            "baro_altitude": aeroplane1.baro_altitude,
        },
    ]


@patch("json.dump")
@patch("json.load")
def test_delete_aeroplane(mock_load, mock_dump, Json_saver, aeroplane1):
    mock_load.return_value = [
        {"test"},
        {
            "callsign": aeroplane1.callsign,
            "origin_country": aeroplane1.origin_country,
            "velocity": aeroplane1.velocity,
            "baro_altitude": aeroplane1.baro_altitude,
        },
    ]
    mock_dump.return_value = None
    assert Json_saver.delete_aeroplane(aeroplane1) == [{"test"}]


@patch("json.dump")
@patch("json.load")
def test_delete_aeroplane_error(mock_load, mock_dump, Json_saver, aeroplane1):
    mock_load.return_value = [
        {"callsign": 1, "origin_country": 2, "velocity": 3, "baro_altitude": 4}
    ]
    mock_dump.return_value = None
    with pytest.raises(ValueError) as e:
        Json_saver.delete_aeroplane(aeroplane1)
    assert str(e.value) == "Самолета нет в файле"


@patch("json.load")
def test_get_top(mock_load, Json_saver):
    mock_load.return_value = [{"test"}, {"test"}, {"test"}, {"test"}, {"test"}]
    assert Json_saver.get_top(5) == [{"test"}, {"test"}, {"test"}, {"test"}, {"test"}]


@patch("json.load")
def test_get_top_error(mock_load, Json_saver):
    mock_load.return_value = [{"test"}, {"test"}, {"test"}, {"test"}, {"test"}]
    with pytest.raises(ValueError) as e:
        Json_saver.get_top(0)
    assert str(e.value) == "Количество должно быть больше нуля"
