from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/Nadja/Development/chromedriver"
TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_PASSWORD = os.environ.get("PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        signin_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
        signin_button.click()
        time.sleep(2)
        email_field = self.driver.find_element(By.TAG_NAME, "input")
        email_field.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-ywje51.r-184id4b.r-13qz1uu.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        next_button.click()
        # try:
        #     time.sleep(2)
        #     password_field = self.driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")
        #     password_field.send_keys(TWITTER_PASSWORD)
        # except:
        #     time.sleep(2)
        #     username_field = self.driver.find_element(By.TAG_NAME, "input")
        #     username_field.send_keys("JelenaPasa75286")
        #     time.sleep(2)
        #     next_button = self.driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        #     next_button.click()
        #     time.sleep(2)
        #     password_field = self.driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")
        #     password_field.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        username_field = self.driver.find_element(By.TAG_NAME, "input")
        username_field.send_keys("JelenaPasa75286")
        time.sleep(2)
        next_button = self.driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        next_button.click()
        time.sleep(2)
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input.r-30o5oe.r-1dz5y72.r-13qz1uu.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-fdjqy7")
        password_field.send_keys(TWITTER_PASSWORD)

        login_button = self.driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        login_button.click()
        time.sleep(3)

        post_field = self.driver.find_element(By.CSS_SELECTOR, "div.notranslate.public-DraftEditor-content")
        post_field.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        post_button = self.driver.find_element(By.CSS_SELECTOR, "button.css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-1cwvpvk.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
        post_button.click()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
print(f"Down: {twitter_bot.down}")
print(f"Up: {twitter_bot.up}")
twitter_bot.tweet_at_provider()
