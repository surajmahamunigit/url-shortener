from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.db.database import get_db
from app.models.user import User
from app.utils.security import verify_password, hash_password, create_access_token

router = APIRouter()


@router.post("/register")
def register(request_form: RegisterRequest, db: Session = Depends(get_db)):

    username = request_form.username
    password = request_form.password

    user = db.query(User).filter(User.username == username)

    if user is not None:
        raise HTTPException(status_code=401, detail="Username already exists")

    hashed_password = hash_password(password)

    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}
