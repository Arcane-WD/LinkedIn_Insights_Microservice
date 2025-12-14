from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.services.page_service import get_or_create_company
from app.models import CompModel

router = APIRouter(prefix="/companies")

def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
         db.close()

@router.get("/")
def list_all_companies(
     db: Session = Depends(get_db)
):
     return (
          db.query(CompModel).all()
     )

@router.get("/search")
def search_companies(
    db: Session = Depends(get_db),
    industry: str | None = None,
    min_size: int | None = None,
    max_size: int | None = None,
    limit: int = 10,
    offset: int = 0,
):
    query = db.query(CompModel)

    if industry:
        query = query.filter(CompModel.industry.ilike(f"%{industry}%"))

    if min_size is not None:
        query = query.filter(CompModel.company_size_min >= min_size)

    if max_size is not None:
        query = query.filter(
            (CompModel.company_size_max <= max_size) |
            (CompModel.company_size_max.is_(None))
        )

    return query.offset(offset).limit(limit).all()


@router.get("/{page_id}")
def get_comp_by_title(
     page_id:str,
     db:Session = Depends(get_db)):
    return get_or_create_company(page_id=page_id, db=db)

