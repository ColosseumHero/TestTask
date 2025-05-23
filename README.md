Incident Management API

A Django REST API for managing incidents with map integration, supporting CRUD operations and GeoJSON output for active incidents.

Features

1. CRUD operations for incidents (ID, title, latitude, longitude, created_at, status).

2. GeoJSON endpoint for map visualization (/api/incidents/geojson/).

3. PostgreSQL database via Docker.

4. Swagger documentation (/swagger/).

Prerequisites

1. Docker

2. Docker Compose

3. Postman (for API testing)

Setup and Run

1. Unzip the Archive

2. Extract the archive to a folder (e.g., TestTask2205).

3. Run with Docker
   
    Navigate to the project folder:
        docker-compose up --build
4. The API will be available at http://localhost:8000/api/incidents/.

5. Swagger documentation: http://localhost:8000/swagger/.

API Endpoints

    GET /api/incidents/: List all incidents.

    POST /api/incidents/: Create an incident.

    GET /api/incidents//: Get incident by ID.

    PUT /api/incidents//: Update incident.

    DELETE /api/incidents//: Delete incident.

    GET /api/incidents/geojson/: Get active incidents in GeoJSON format.

Testing example
    
POST http://localhost:8000/api/incidents/
    Content-Type: application/json
    
    {
        "title": "Test Incident",
        "latitude": 50.5,
        "longitude": 30.5,
        "status": "ACTIVE"
    }

Stop Containers

    docker-compose down
