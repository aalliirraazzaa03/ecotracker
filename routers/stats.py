from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, database

router = APIRouter(prefix="/stats", tags=["stats"])

@router.get("/{user_id}")
def total_carbon(user_id: int, db: Session = Depends(database.get_db)):
    total = crud.get_total_carbon(db, user_id)
    return {"user_id": user_id, "total_carbon_kg": total}
