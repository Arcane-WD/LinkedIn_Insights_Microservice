from sqlalchemy.orm import Session
from app.models import CompModel
from app.services.scrapper.company_scraper import company_scrapper


def get_or_create_company(page_id:str, db: Session):
    comp = (
        db.query(CompModel).filter(CompModel.page_id==page_id).first()
    )

    if comp:
        return comp
    
    data = company_scrapper(page_id)

    comp = CompModel(**data)
    db.add(comp)
    db.commit()
    db.refresh(comp)  

    return comp
    