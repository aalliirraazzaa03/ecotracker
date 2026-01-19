EcoTracker API

EcoTracker is a FastAPI backend that allows users to track their carbon footprint and environmental activities. Users can log activities such as transportation, energy usage, and recycling, and view statistics about their personal environmental impact.

This project is designed as a production-ready backend with REST APIs, ready to connect to a frontend (React, Vue, or any client).

Features

Users – Register and manage users.

Activities – Log environmental actions with carbon impact.

Stats – Calculate total carbon footprint per user.

REST API – Fully functional CRUD endpoints.

SQLite Database – Lightweight and easy to use.

Interactive Docs – Swagger UI at /docs and ReDoc at /redoc.

Project Structure
ecotracker_api/
├─ main.py            # Entry point
├─ database.py        # Database connection
├─ models.py          # SQLAlchemy models
├─ schemas.py         # Pydantic schemas
├─ crud.py            # CRUD operations
├─ routers/           # API routers
│   ├─ __init__.py
│   ├─ users.py
│   ├─ activities.py
│   └─ stats.py
└─ ecotracker.db      # SQLite database

Installation

Clone the repository:

git clone https://github.com/aalliirraazzaa03/ecotracker.git
cd ecotracker


Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux


Install dependencies:

pip install fastapi uvicorn sqlalchemy pydantic

Running the Server
uvicorn main:app --reload


Server will run at: http://127.0.0.1:8000

Swagger API docs: http://127.0.0.1:8000/docs

ReDoc API docs: http://127.0.0.1:8000/redoc

API Endpoints
Users

POST /users/ – Create a new user

GET /users/ – List all users

Activities

POST /activities/ – Log a new activity

GET /activities/{user_id} – Get activities for a specific user

Stats

GET /stats/{user_id} – Get total carbon footprint for a user

Example Requests

Create a user:

POST /users/
{
  "username": "alice",
  "email": "alice@example.com"
}


Log an activity:

POST /activities/
{
  "user_id": 1,
  "category": "transport",
  "description": "Bus ride to work",
  "carbon_kg": 2.5
}


Get total carbon:

GET /stats/1


Response:

{
  "user_id": 1,
  "total_carbon_kg": 2.5
}

Database

Uses SQLite (ecotracker.db) for simplicity.

Tables are automatically created on the first run.

Contributing

Fork the repository.

Create a feature branch: git checkout -b feature/my-feature

Commit your changes: git commit -m "Add feature"

Push to the branch: git push origin feature/my-feature

Open a Pull Request.

License

This project is licensed under the MIT License.
