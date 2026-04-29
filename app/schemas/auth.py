from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    """
    Define the shape of the data expected when user regisetres
    """

    # Username must be between 3 and 50 characters
    username: str = Field(..., min_length=3, max_length=50)

    # Password must be between 6 and 72 characters
    password: str = Field(..., min_length=6, max_length=72)


class LoginRequest(BaseModel):
    """
    Defines the shape of the data when user logs in
    """

    username: str
    password: str


class TokenResponse(BaseModel):
    """
    Define the shape of the data returned after successful login.
    """

    access_token: str
    token_type: str
