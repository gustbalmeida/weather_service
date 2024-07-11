from flask import request, jsonify
from app import app, db
from app.models import WeatherData
from app.tasks import fetch_weather_data
import datetime


@app.route('/weather', methods=['POST'])
def add_weather():
    user_id = request.json.get('user_id')
    city_id = request.json.get('city_id')

    if not user_id or not city_id:
        return jsonify({'error': 'Invalid input'}), 400

    existing_entry = WeatherData.query.filter_by(user_id=user_id).first()
    if existing_entry:
        return jsonify({'error': 'User ID already exists'}), 400

    weather_data = WeatherData(user_id=user_id, request_time=datetime.datetime.now(), city_id=city_id, temperature=0,
                               humidity=0)
    db.session.add(weather_data)
    db.session.commit()

    fetch_weather_data.delay(user_id, city_id)

    return jsonify({'message': 'Request accepted'}), 202


@app.route('/weather/<user_id>', methods=['GET'])
def get_weather(user_id):
    data = WeatherData.query.filter_by(user_id=user_id).first()
    if not data:
        return jsonify({'error': 'No data found'}), 404

    return jsonify({
        'user_id': data.user_id,
        'request_time': data.request_time,
        'city_id': data.city_id,
        'temperature': data.temperature,
        'humidity': data.humidity
    }), 200
