# Weather Service

## Description
A Flask-based service to collect weather data using the Open Weather API.

## Setup
### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd weather_service
    ```

2. Build and run the Docker container:
    ```sh
    docker build -t weather_service .
    docker run -d -p 5000:5000 --name weather_service weather_service
    ```

3. Run tests:
    ```sh
    pytest --cov=app tests/
    ```

## Usage
- **POST /weather**: Collect weather data
    ```sh
    curl -X POST http://localhost:5000/weather -d '{"user_id": "unique_id", "city_id": 3448439}' -H "Content-Type: application/json"
    ```

- **GET /weather/<user_id>**: Retrieve weather data
    ```sh
    curl http://localhost:5000/weather/unique_id
    ```

## Configuration
Update `config.py` with your Open Weather API key.