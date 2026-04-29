from sqlalchemy import Column, Integer, String
from app.db.database import Base


class User(Base):
    """
    Represnt the users table in the database
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # Username must be unique across all the users
    username = Column(String, unique=True, index=True, nullable=False)
    # Store hashed password
    password = Column(String, nullable=False)
