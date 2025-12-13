from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import CompModel

app = FastAPI(title="LinkedIn Insights MicroService")

def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
         db.close()

@app.get("/companies")
def get_companies(
     db: Session = Depends(get_db)
):
     return (
          db.query(CompModel).all()
     )


@app.get("/companies/{page_id}")
def get_comp_by_title(
     page_id:str,
     db:Session = Depends(get_db)):
    company = db.query(CompModel).filter(CompModel.page_id==page_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company Not in Database...")
    
    return company
