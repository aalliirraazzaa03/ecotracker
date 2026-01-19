from fastapi import FastAPI
import models, database
from routers import users, activities, stats

app = FastAPI(title="EcoTracker API")

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Include routers
app.include_router(users.router)
app.include_router(activities.router)
app.include_router(stats.router)

@app.get("/")
def root():
    return {"message": "Welcome to EcoTracker API"}
