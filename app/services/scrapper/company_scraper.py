from linkedin_scraper import Company, actions
from selenium import webdriver
from app.services.scrapper.auth import log_in
from app.config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD
import re
import time
from typing import Tuple, Optional

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
    print(f"Scraping: {url}")

    def is_invalid_company_page(driver) -> bool:
        current_url = driver.current_url.lower()
        if "company/unavailable" in current_url:
            return True

        page_source = driver.page_source.lower()
        invalid_markers = [
            "this linkedin page isn’t available",
            "this page doesn’t exist",
            "page not found",
            "profile not found"
        ]

        return any(m in page_source for m in invalid_markers)


    def parse_company_size(size_str: str) -> Tuple[Optional[int], Optional[int]]:
        if not size_str:
            return None, None

        s = size_str.lower()

        # "10,001+ employees"
        if "+" in s:
            num = int(re.sub(r"[^\d]", "", s))
            return num, None

        # "2-10 employees"
        if "-" in s:
            nums = re.findall(r"\d+", s)
            if len(nums) == 2:
                return int(nums[0]), int(nums[1])

        # fallback: single number
        nums = re.findall(r"\d+", s)
        if nums:
            n = int(nums[0])
            return n, n

        return None, None

    
    driver.get(url)
    time.sleep(2)

    if is_invalid_company_page(driver):
        driver.quit()
        return None

    company = Company(
        linkedin_url=url,
        driver=driver,
        scrape=True,
        get_employees=False,
        close_on_complete=False
    )
    min_size, max_size = parse_company_size(company.company_size)
    company_data = {
        "page_id": company_id,
        "name": company.name,
        "linkedin_url": url,
        "about_us": company.about_us,
        "industry": company.industry,
        "company_type": company.company_type,
        "company_size_raw": company.company_size,
        "company_size_min": min_size,
        "company_size_max": max_size,
        "headcount": company.headcount,
        "website": company.website,
        "phone": company.phone,
        "headquarters": company.headquarters,
        "founded": company.founded,
        "specialties": company.specialties,
    }

    driver.quit()

    return company_data
    


