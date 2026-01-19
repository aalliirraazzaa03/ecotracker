from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter(prefix="/activities", tags=["activities"])

@router.post("/", response_model=schemas.Activity)
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(database.get_db)):
    return crud.create_activity(db, activity)

@router.get("/{user_id}", response_model=list[schemas.Activity])
def get_user_activities(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_activities(db, user_id)
