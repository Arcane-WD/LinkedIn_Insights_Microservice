from fastapi import FastAPI

from app.api.pages import router as companies_router

app = FastAPI(title="LinkedIn Insights MicroService")

app.include_router(companies_router)

