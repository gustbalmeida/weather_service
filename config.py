import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'weather.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
OPEN_WEATHER_API_KEY = '7a1d43faa60c4900963bb922610d3a12'