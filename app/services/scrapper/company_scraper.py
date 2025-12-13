from linkedin_scraper import Company, actions
from selenium import webdriver


def company_scrapper(company_id:str):
        
    driver = webdriver.Chrome()

    email = "vrhr.olsi@gmail.com"
    pwd = "Harrsha_J@1911"

    #Login
    actions.login(driver=driver, email=email, password=pwd)

    url = "https://www.linkedin.com/company/" + company_id
    print(f"Scraping: {url}")

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
    


