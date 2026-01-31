from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth import LoginRequest
from app.services.auth import authenticate_user
from app.core.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.email, data.password)

    token = create_access_token(subject=str(user.id))
    return {
        "access_token": token,
        "token_type": "bearer"
    }
