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

    def to_dict(self):
        return {
            "page_id": self.page_id,
            "name": self.name,
            "linkedin_url": self.linkedin_url,
            "about_us": self.about_us,
            "industry": self.industry,
            "company_type": self.company_type,
            "company_size_raw": self.company_size_raw,
            "company_size_min": self.company_size_min,
            "company_size_max": self.company_size_max,
            "headcount": self.headcount,
            "website": self.website,
            "phone": self.phone,
            "headquarters": self.headquarters,
            "founded": self.founded,
            "specialties": self.specialties,
            "is_valid": self.is_valid,
        }
