from celery import Celery
from app import app, db
from app.models import WeatherData
import requests

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

celery = make_celery(app)

@celery.task
def fetch_weather_data(user_id, city_id):
    api_key = app.config['OPEN_WEATHER_API_KEY']
    url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    weather_data = WeatherData.query.filter_by(user_id=user_id).first()
    if weather_data:
        weather_data.temperature = data['main']['temp']
        weather_data.humidity = data['main']['humidity']
        db.session.commit()
