from app.database import Base
from sqlalchemy import Column, Integer, String, Text

class CompModel(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    page_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    linkedin_url = Column(String)

    about_us = Column(Text)
    industry = Column(String)
    company_type = Column(String)
    company_size = Column(String)
    headcount = Column(Integer)

    website = Column(String)
    phone = Column(String)
    headquarters = Column(String)
    founded = Column(String)

    specialties = Column(Text) 