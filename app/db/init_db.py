from app.db.database import engine, Base
from app.models.user import User
from app.models.link import Link


def init_db():
    """
    Creates all database tables on startup if they dont already exist.
    """

    Base.metadata.create_all(bind=engine)
