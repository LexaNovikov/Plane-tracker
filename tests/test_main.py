from unittest.mock import patch

import pytest

from main import filter_aeroplanes, quick_sort, user_interaction, sort_aeroplanes, get_top_aeroplanes, print_aeroplanes, get_aeroplanes_by_altitude
def test_filter_aeroplanes(planes):
    result = filter_aeroplanes(planes, "United States")[0]
    assert result.origin_country == "United States"

def test_quick_sort(planes):
    result = quick_sort(planes, 0, 4)
    for i in range(1, 5):
        assert result[i].baro_altitude <= result[i - 1].baro_altitude

def test_sort_aeroplanes(planes):
    result = sort_aeroplanes(planes)
    for i in range(1, 5):
        assert result[i].baro_altitude <= result[i - 1].baro_altitude
def test_get_aeroplanes_by_altitude(planes):
    result = get_aeroplanes_by_altitude(planes, "10000 - 20000")
    for i in range(1, len(result)):
        assert 10000 <= result[i].baro_altitude <= 20000
def test_get_top_aeroplanes_error(planes):
    with pytest.raises(ValueError) as e:
        get_top_aeroplanes(planes, 0)
    assert str(e.value) == "Количество не может быть меньше единицы"
@patch('builtins.input')
def test_user_interaction(mock_input):
    mock_input.side_effect = [
        "Russia",
        "5",
        "Germany",
        "0 - 10000"
    ]
    user_interaction()
    assert mock_input.call_count == 4


