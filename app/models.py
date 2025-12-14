from app.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean

class CompModel(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    page_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    linkedin_url = Column(String)

    about_us = Column(Text)
    industry = Column(String)
    company_type = Column(String)
    company_size_raw = Column(String)
    company_size_min = Column(Integer, index=True)  
    company_size_max = Column(Integer)   
    headcount = Column(Integer)

    website = Column(String)
    phone = Column(String)
    headquarters = Column(String)
    founded = Column(String)

    specialties = Column(Text)
    is_valid = Column(Boolean, default=True)
