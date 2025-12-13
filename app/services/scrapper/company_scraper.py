from linkedin_scraper import Company, actions
from selenium import webdriver
from app.services.scrapper.auth import log_in
from app.config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD

def company_scrapper(company_id:str):
        
    driver = webdriver.Chrome()
    print("EMAIL:", LINKEDIN_EMAIL)
    print("PASSWORD:", "SET" if LINKEDIN_PASSWORD else "MISSING")

    log_in(
        driver=driver,
        email = LINKEDIN_EMAIL,
        pwd=LINKEDIN_PASSWORD
    )

    url = "https://www.linkedin.com/company/" + company_id
    driver.get(url)

    if "Page not found" in driver.page_source:
        return None
    
    print(f"Scraping: {url}")
    def parse_company_size(size_str: str):
        if not size_str:
            return None

        number_part = size_str.split()[0]  # "10,001+"
        number_part = number_part.replace("+", "").replace(",", "")
        return int(number_part)
    


    company = Company(
        linkedin_url=url,
        driver=driver,
        scrape=True,
        get_employees=False,
        close_on_complete=False
    )

    company_data = {
        "page_id": company_id,
        "name": company.name,
        "linkedin_url": url,
        "about_us": company.about_us,
        "industry": company.industry,
        "company_type": company.company_type,
        "company_size": company.company_size,
        "headcount": company.headcount,
        "website": company.website,
        "phone": company.phone,
        "headquarters": company.headquarters,
        "founded": company.founded,
        "specialties": company.specialties,
    }

    driver.quit()

    return company_data
    


