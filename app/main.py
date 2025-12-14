from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

from fastapi import FastAPI

from app.api.pages import router as companies_router
from app.database import Base, engine 
from app import models                  

Base.metadata.create_all(bind=engine)
app = FastAPI(title="LinkedIn Insights MicroService")
app.include_router(companies_router)

