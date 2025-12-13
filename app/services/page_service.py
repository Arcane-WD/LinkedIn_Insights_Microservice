from linkedin_scraper import Person, actions
from selenium import webdriver
driver = webdriver.Chrome()

email = "xxx.com"
password = "xxx"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal

company_url_header = "https://www.linkedin.com/company"

print(person)

link = input()
link = link.split("/")
account_type = link[3]
print(account_type)
