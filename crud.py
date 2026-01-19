from sqlalchemy.orm import Session
import models, schemas

# Users
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Activities
def create_activity(db: Session, activity: schemas.ActivityCreate):
    db_activity = models.Activity(**activity.model_dump())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def get_activities(db: Session, user_id: int):
    return db.query(models.Activity).filter(models.Activity.user_id == user_id).all()

# Stats
def get_total_carbon(db: Session, user_id: int):
    result = db.query(models.Activity).filter(models.Activity.user_id == user_id).all()
    return sum(a.carbon_kg for a in result)
