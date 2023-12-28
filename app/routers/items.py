from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.item import Item
from ..services.item import get_items

router = APIRouter()


@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    if items is None:
        raise HTTPException(status_code=404, detail="Items not found")
    return items
