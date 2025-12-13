from linkedin_scraper import Company, actions
from selenium import webdriver
driver = webdriver.Chrome()
import time
import json

email = "vrhr.olsi@gmail.com"
password = "Harrsha_J@1911"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal

company_url_header = "https://www.linkedin.com/company/"

companies = ["google", "microsoft", "deepsolv", "oracle", "meta", "electronic-arts"]

results = []

for comp in companies:
    url = company_url_header+comp
    print(f"Scraping: {url}")

    company = Company(
        linkedin_url=url,
        driver=driver,
        scrape=True,
        get_employees=False,
        close_on_complete=False
    )

    time.sleep(3)

    company_data = {
        "page_id": comp,
        "name": company.name,
        "linkedin_url": url,

        # Core details
        "about_us": company.about_us,
        "industry": company.industry,
        "company_type": company.company_type,
        "company_size": company.company_size,
        "headcount": company.headcount,

        # Contact / metadata
        "website": company.website,
        "phone": company.phone,
        "headquarters": company.headquarters,
        "founded": company.founded,

        # Lists (store as-is for now)
        "specialties": company.specialties,
    }

    results.append(company_data)

driver.quit()


with open("companies.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
