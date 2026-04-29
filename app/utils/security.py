from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import SECRET_KEY, ALGORITHM
from app.db.database import get_db
from app.models.user import User

# Configues bcrypt for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Reads JWT token from the Authorization header of incoming request
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def hash_password(password: str) -> str:
    """
    Takes plain text password and returns a bcrypt hashed vesrion
    """

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compares the plain password against the hashed passsword
    Returns True if they match, False if they dont
    """

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Creates a signed JWT token containing the provided data
    Token expires after 30 minutes
    """

    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})

    # Sign the token with our SECRET_KEY from .env
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    """
    Reads the JWT token from the request, decodes it, and returns the current user
    Raises 401 if the token is invalid, expired, or the user doesnt exist
    """
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate the credentials."
    )

    try:
        # Decodes and verifies the token for signature and expiry
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise credentials_exception

    return user
