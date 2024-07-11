import pytest
from app import app, db
from app.models import WeatherData
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_add_weather(client):
    response = client.post('/weather', json={'user_id': 'unique_user_id'})
    assert response.status_code == 202
    data = json.loads(response.data)
    assert data['message'] == 'Weather data added successfully'

def test_add_weather_duplicate(client):
    client.post('/weather', json={'user_id': 'unique_user_id'})
    response = client.post('/weather', json={'user_id': 'unique_user_id'})
    assert response.status_code == 400

def test_get_weather(client):
    client.post('/weather', json={'user_id': 'unique_user_id'})
    response = client.get('/weather/unique_user_id')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'city_id' in data
    assert 'temperature' in data
    assert 'humidity' in data

def test_get_weather_not_found(client):
    response = client.get('/weather/non_existent_user_id')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['message'] == 'User ID not found'
