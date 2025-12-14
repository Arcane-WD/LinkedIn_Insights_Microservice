from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import CompModel
from app.services.scrapper.company_scraper import company_scrapper


def get_or_create_company(page_id:str, db: Session):
    comp = db.query(CompModel).filter(CompModel.page_id == page_id).first()

    if comp:
        if not comp.is_valid:
            raise HTTPException(status_code=404, detail="LinkedIn page not found")
        return comp
    
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

    return comp
    