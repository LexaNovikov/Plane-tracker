from unittest.mock import patch

from src.connect_class import AbcAeroplanesAPI


def test_init(API):
    assert API.country_name == "Russia"
    assert issubclass(type(API), AbcAeroplanesAPI)


@patch("requests.get")
def test_get_country_cords(mock_get, API):
    mock_get.return_value.json.return_value = {"features": [{"bbox": [0, 1, 2, 3]}]}
    assert API.get_country_cords() == (1, 3, 0, 2)


@patch("opensky_api.OpenSkyApi.get_states")
@patch("requests.get")
@patch("opensky_api.TokenManager.from_json_file")
def test_get_aeroplanes(mock_token_manager, mock_requests_get, mock_get_states, API):
    mock_token_manager.return_value = ""
    mock_requests_get.return_value.json.return_value = {
        "features": [{"bbox": [0, 1, 2, 3]}]
    }
    mock_get_states.return_value.states = (1, 2, 3)
    assert API.get_aeroplanes() == (1, 2, 3)
    mock_token_manager.assert_called_once()
