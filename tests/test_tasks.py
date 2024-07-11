import pytest
from unittest.mock import patch
from app.tasks import fetch_weather_data


def test_fetch_weather_data_success():
    api_key = 'test_api_key'
    city_id = '3448439'
    mock_response = {
        'main': {
            'temp': 25,
            'humidity': 80
        },
        'id': city_id
    }

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = fetch_weather_data(city_id, api_key)
        assert result == mock_response


def test_fetch_weather_data_failure():
    api_key = 'test_api_key'
    city_id = '3448439'

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        with pytest.raises(requests.exceptions.HTTPError):
            fetch_weather_data(city_id, api_key)
