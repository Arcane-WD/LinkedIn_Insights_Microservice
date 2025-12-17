from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import CompModel
from app.services.scrapper.company_scraper import company_scrapper
import json
from app.cache.cache import redis



async def get_or_create_company(page_id:str, db: Session):
    CACHE_TTL = 60 * 60  # 1 hour

    cache_key = f"Company:{page_id}"
    cached = await redis.get(cache_key)
    if cached:
        return json.loads(cached)
    
    comp = db.query(CompModel).filter(CompModel.page_id == page_id).first()

    if comp:
        if not comp.is_valid:
            raise HTTPException(status_code=404, detail="LinkedIn page not found")
        
        data = comp.to_dict()
        await redis.set(cache_key,json.dumps(data),ex=CACHE_TTL)

        return data
    
    data = company_scrapper(page_id)

    if data is None:
        invalid_comp = CompModel(
            page_id=page_id,
            is_valid=False
        )
        db.add(invalid_comp)
        db.commit()

        raise HTTPException(
            status_code=404,
            detail="LinkedIn page not found"
        )

    
    comp = CompModel(**data)
    db.add(comp)
    db.commit()
    db.refresh(comp)  
    data = comp.to_dict()
    await redis.set(cache_key, json.dumps(data), ex=CACHE_TTL)
    return data
    