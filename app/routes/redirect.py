from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.link import Link

router = APIRouter()


@router.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    """
    Redirects to the original URL for the given short code
    Increments the click count by 1 every time link is visited.
    """

    link = db.query(Link).filter(Link.short_code == short_code).first()

    if link is None:
        raise HTTPException(status_code=404, detail="Short link not found in db")

    link.click_count += 1
    db.commit()

    return RedirectResponse(url=link.original_url, status_code=307)
