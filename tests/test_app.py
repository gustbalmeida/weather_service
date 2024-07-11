import pytest
from app import app, db
from app.models import WeatherData

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_add_weather(client):
    response = client.post('/weather', json={'user_id': 'test_user_1', 'city_id': 3448439})
    assert response.status_code == 202

def test_get_weather(client):
    client.post('/weather', json={'user_id': 'test_user_2', 'city_id': 3448439})
    response = client.get('/weather/test_user_2')
    assert response.status_code == 200
