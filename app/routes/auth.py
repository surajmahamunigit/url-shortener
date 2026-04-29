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

    user = db.query(User).filter(User.username == username).first()

    if user is not None:
        raise HTTPException(status_code=401, detail="Username already exists")

    hashed_password = hash_password(password)

    new_user = User(username=username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):

    username = data.username
    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    access_token = create_access_token(data={"sub": username})

    return TokenResponse(access_token=access_token, token_type="bearer")
