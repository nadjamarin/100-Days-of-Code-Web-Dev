from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(num_articles.text)

# Click on links (and buttons) using Selenium
# num_articles.click()

# Find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Type into search bar
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
# Hitting "Enter" to search
# Need to use Keys class from selenium
search.send_keys(Keys.ENTER)

