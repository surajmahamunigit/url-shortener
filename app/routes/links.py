import secrets
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.link import Link
from app.models.user import User
from app.schemas.link import LinkCreate, LinkResponse, StatsResponse
from app.utils.security import get_current_user

router = APIRouter(prefix="/links", tags=["Links"])


@router.post("/shorten", response_model=LinkResponse)
def create_link(
    data: LinkCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Creates a new short link for the logged in user.
    """

    while True:
        short_code = secrets.token_urlsafe(6)
        existing = db.query(Link).filter(Link.short_code == short_code).first()

        if not existing:
            break

    new_link = Link(
        original_url=str(data.original_url),
        short_code=short_code,
        user_id=current_user.id,
    )

    db.add(new_link)
    db.commit()
    db.refresh(new_link)

    return new_link


@router.get("/my-links", response_model=list[LinkResponse])
def get_my_links(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    """
    Returns all the links created by logged in user
    """

    links = db.query(Link).filter(Link.user_id == current_user.id).all()

    return links


@router.get("/stats/{short_code}", response_model=StatsResponse)
def get_stats(
    short_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Returns stats for specific short link owned by the logged in user.
    """

    link = db.query(Link).filter(Link.short_code == short_code).first()

    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")

    # Only owner can see the stats of their own links
    if link.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized ")

    return link


@router.delete("/{short_code}")
def delete_link(
    short_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Deletes the short link owned by the logged in user.
    """

    link = db.query(Link).filter(Link.short_code == short_code).first()

    if link is None:
        raise HTTPException(status_code=404, detail="Link not found")

    # Only owner can delete it
    if link.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db.delete(link)
    db.commit()

    return {"message": "Link deleted successfully"}
