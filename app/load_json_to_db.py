import json
from database import SessionLocal
from models import CompModel

db = SessionLocal()

import json
import os


with open("scripts/companies.json", "r", encoding="utf-8") as f:
    companies = json.load(f)


def parse_company_size(size_str: str):
    if not size_str:
        return None

    number_part = size_str.split()[0]  # "10,001+"
    number_part = number_part.replace("+", "").replace(",", "")
    return int(number_part)


for c in companies:
    company = CompModel(
        page_id=c["page_id"],
        name=c["name"],
        linkedin_url=c["linkedin_url"],
        about_us=c["about_us"],
        industry=c["industry"],
        company_type=c["company_type"],
        company_size=parse_company_size(c["company_size"]),
        headcount=c["headcount"],
        website=c["website"],
        phone=c["phone"],
        headquarters=c["headquarters"],
        founded=c["founded"],
        specialties=c["specialties"]
    )

    db.add(company)

db.commit()
db.close()