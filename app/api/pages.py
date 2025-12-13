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

@router.get("/{page_id}")
def get_comp_by_title(
     page_id:str,
     db:Session = Depends(get_db)):
    return get_or_create_company(page_id=page_id, db=db)