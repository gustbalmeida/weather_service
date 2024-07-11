# Weather Service

## Description
A Flask-based service to collect weather data using the Open Weather API. The service collects weather data for specified city IDs and stores it in a SQLite database. It also supports asynchronous data collection using Celery and Redis.

## Setup

### Prerequisites
- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gustbalmeida/weather_service.git
    cd weather_service
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

3. Run tests:
    ```sh
    docker exec -it weather_service pytest --cov=app tests/
    ```

## Usage

### Endpoints

- **POST /weather**: Collect weather data
    ```sh
    curl -X POST http://localhost:5000/weather -d '{"user_id": "unique_id", "city_id": 3448439}' -H "Content-Type: application/json"
    ```

- **GET /weather/<user_id>**: Retrieve weather data
    ```sh
    curl http://localhost:5000/weather/unique_id
    ```

### Configuration

Update `config.py` with your Open Weather API key.

### Environment Variables

You can also set environment variables in the `docker-compose.yml` file:
- `OPEN_WEATHER_API_KEY`: Your Open Weather API key.
- `REDIS_URL`: The URL of the Redis server (default is `redis://redis:6379/0`).

## Architecture

- **Flask**: The web framework used to create the API.
- **SQLAlchemy**: ORM for interacting with the SQLite database.
- **Celery**: Task queue for handling asynchronous tasks.
- **Redis**: Message broker for Celery tasks.
- **Docker**: Containerization of the application and its dependencies.

## Docker Compose Services

- **weather_service**: The Flask application.
- **redis**: The Redis server for Celery.

## Running the Application

To start the application, simply use Docker Compose:
```sh
docker-compose up
