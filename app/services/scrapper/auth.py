import os
import pickle
import time
from linkedin_scraper import actions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pathlib import Path
COOKIE_FILE = Path(__file__).parent / "linkedin_cookies.pkl"


def save_cookies(driver):
    with open(COOKIE_FILE, "wb") as f:
        pickle.dump(driver.get_cookies(), f)

def load_cookies(driver):
    if not COOKIE_FILE.exists():
        return False

    driver.get("https://www.linkedin.com")
    with open(COOKIE_FILE, "rb") as f:
        cookies = pickle.load(f)

    for cookie in cookies:
        cookie.pop("sameSite", None)
        driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(2)

    return True

def log_in(driver, email=None, pwd=None):
    cookies_loaded = load_cookies(driver)

    if cookies_loaded and is_logged_in(driver):
        return

    if not email or not pwd:
        raise RuntimeError("Cookies invalid and no credentials provided")

    actions.login(driver, email=email, password=pwd)
    time.sleep(8)

    if not is_logged_in(driver):
        raise RuntimeError("Login failed")

    save_cookies(driver)

def is_logged_in(driver):
    try:
        driver.find_element(By.ID, "global-nav")
        return True
    except NoSuchElementException:
        return False