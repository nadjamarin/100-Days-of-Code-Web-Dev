import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Challenge: Use selenium to type first name, last name, and email into test website
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

cursor = driver.find_element(By.ID, value="buyCursor")
grandma = driver.find_element(By.ID, value="buyGrandma")
factory = driver.find_element(By.ID, value="buyFactory")
mine = driver.find_element(By.ID, value="buyMine")
shipment = driver.find_element(By.ID, value="buyShipment")
alchemy_lab = driver.find_element(By.ID, value="buyAlchemy lab")
portal = driver.find_element(By.ID, value="buyPortal")
time_machine = driver.find_element(By.ID, value="buyTime machine")

# cookie_counter = driver.find_element(By.ID, value="money")

initial_time = time.perf_counter()
play_time = time.perf_counter()

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

# while play_time - initial_time < 300:
while True:
    play_time = time.perf_counter()
    cookie.click()

    num_cookies = int(driver.find_element(By.ID, value="money").text.replace(',', ''))

    # cursor_price = int(cursor.text.split()[2].replace(',', ''))
    # grandma_price = int(grandma.text.split()[2].replace(',', ''))
    # factory_price = int(factory.text.split()[2].replace(',', ''))
    # mine_price = int(mine.text.split()[2].replace(',', ''))
    # shipment_price = int(shipment.text.split()[2].replace(',', ''))
    # alchemy_lab_price = int(alchemy_lab.text.split()[3].replace(',', ''))
    # portal_price = int(portal.text.split()[2].replace(',', ''))
    # time_machine_price = int(time_machine.text.split()[3].replace(',', ''))

    # if round(play_time) % 5 == 0:
    if time.time() > timeout:
        if num_cookies > int(time_machine.text.split()[3].replace(',', '')):
            time_machine.click()
        elif num_cookies > int(portal.text.split()[2].replace(',', '')):
            portal.click()
        elif num_cookies > int(alchemy_lab.text.split()[3].replace(',', '')):
            alchemy_lab.click()
        elif num_cookies > int(shipment.text.split()[2].replace(',', '')):
            shipment.click()
        elif num_cookies > int(mine.text.split()[2].replace(',', '')):
            mine.click()
        elif num_cookies > int(factory.text.split()[2].replace(',', '')):
            factory.click()
        elif num_cookies > int(grandma.text.split()[2].replace(',', '')):
            grandma.click()
        elif num_cookies > int(cursor.text.split()[2].replace(',', '')):
            cursor.click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

        # if num_cookies > time_machine_price:
        #     time_machine.click()
        # elif num_cookies > portal_price:
        #     portal.click()
        # elif num_cookies > alchemy_lab_price:
        #     alchemy_lab.click()
        # elif num_cookies > shipment_price:
        #     shipment.click()
        # elif num_cookies > mine_price:
        #     mine.click()
        # elif num_cookies > factory_price:
        #     factory.click()
        # elif num_cookies > grandma_price:
        #     grandma.click()
        # elif num_cookies > cursor_price:
        #     cursor.click()

cookies_per_second = driver.find_element(By.ID, value="cps").text
print(cookies_per_second)
driver.quit()


