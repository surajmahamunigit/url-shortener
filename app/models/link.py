from sqlalchemy import Integer, String, Column
from app.db.database import Base


class Link(Base):
    """
    Represents the links table in the database
    """

    id = Column(Integer, unique=True, index=True)
    # Cant be empty
    original_url = Column(String, nullable=False)

    # Short code must be unique across all the links
    short_code = Column(String, unique=True, index=True, nullable=False)

    # Starts at 0 when new link is created
    click_count = Column(Integer, efault=0, nullable=False)

    # Foreign key
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
