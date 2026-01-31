from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth import LoginRequest
from app.services.auth import authenticate_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/auth")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.email, data.password)
    return {
        "message": "Login Succesful",
        "user_id": user.id
    }
