from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3918564565&f_AL=true&keywords=biomedical%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

# Redirect to sign in screen
login_button = driver.find_element(By.CLASS_NAME, value="job-alert-redirect-section__cta")
login_button.click()

# Sign in to LinkedIn
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys(email)
password_field.send_keys(password)

signin_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
signin_button.click()

# Use Selenium to apply for jobs
apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
apply_button.click()

first_next_button = driver.find_element(By.CSS_SELECTOR, ".ph5 button")
first_next_button.click()
time.sleep(3)
second_next_button = driver.find_element(By.CSS_SELECTOR, ".display-flex.justify-flex-end.ph5.pv4 button(2)")
second_next_button.click()

