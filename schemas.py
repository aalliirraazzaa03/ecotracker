from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        from_attributes = True  # For Pydantic v2

# Activity Schemas
class ActivityBase(BaseModel):
    category: str
    description: Optional[str] = None
    carbon_kg: float

class ActivityCreate(ActivityBase):
    user_id: int

class Activity(ActivityBase):
    id: int
    user_id: int
    created_at: datetime
    class Config:
        from_attributes = True
