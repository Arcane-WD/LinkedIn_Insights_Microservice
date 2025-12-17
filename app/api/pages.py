from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.services.page_service import get_or_create_company
from app.models import CompModel
import json
from app.cache.cache import redis
from app.cache.cache_keys import make_search_cache_key

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
          db.query(CompModel).filter(CompModel.is_valid==True).all()
     )

@router.get("/search")
async def search_companies(
    db: Session = Depends(get_db),
    industry: str | None = None,
    min_size: int | None = None,
    max_size: int | None = None,
    limit: int = 10,
    offset: int = 0,
):
    SEARCH_CACHE_TTL = 300
    cache_key = make_search_cache_key(
        industry=industry,
        min_size=min_size,
        max_size=max_size,
        limit=limit,
        offset=offset,
    )

    cached = await redis.get(cache_key)
    if cached:
        return json.loads(cached)

    query = db.query(CompModel).filter(CompModel.is_valid==True)

    if industry:
        query = query.filter(CompModel.industry.ilike(f"%{industry}%"))

    if min_size is not None:
        query = query.filter(CompModel.company_size_min >= min_size)

    if max_size is not None:
        query = query.filter(
            (CompModel.company_size_max <= max_size) |
            (CompModel.company_size_max.is_(None))
        )

    companies = query.offset(offset).limit(limit).all()
    data = [company.to_dict() for company in companies]
    await redis.set(
    cache_key,
    json.dumps(data),
    ex=SEARCH_CACHE_TTL
)
    return data


@router.get("/{page_id}")
async def get_comp_by_title(
     page_id:str,
     db:Session = Depends(get_db)):
    return await get_or_create_company(page_id=page_id, db=db)

