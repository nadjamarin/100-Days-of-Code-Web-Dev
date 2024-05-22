from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import os
import time
from pprint import pprint

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScvI8AJyqzJsXcAnhx0LP_BZiaCxgFtgYoqHZZ0KVkDUkAewQ/viewform?usp=sf_link"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(ZILLOW_URL)
zillow_webpage = response.text

# Beautiful Soup
soup = BeautifulSoup(zillow_webpage, "html.parser")

links = soup.select(selector=".property-card-link")
listing_links = [link.get("href") for link in links]

prices = soup.select(selector=".PropertyCardWrapper__StyledPriceLine")
listing_prices = [price.getText()[:6] for price in prices]

addresses = soup.select(selector="address")
listing_addresses = [address.text.strip().replace('|', '') for address in addresses]

# Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(0, 10):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)

    address_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_entry.send_keys(listing_addresses[i])
    time.sleep(1)
    price_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_entry.send_keys(listing_prices[i])
    time.sleep(1)
    link_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_entry.send_keys(listing_links[i])

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_button.click()

driver.quit()
