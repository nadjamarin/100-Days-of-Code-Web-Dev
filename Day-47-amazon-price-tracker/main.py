import requests
from bs4 import BeautifulSoup
import smtplib
# from unidecode import unidecode

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGET_PRICE = 100.0

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=URL, headers=headers)
amazon_webpage = response.text
# print(amazon_webpage)

soup = BeautifulSoup(amazon_webpage, "lxml")
price_dollars = soup.find(name="span", class_="a-price-whole")
price_cents = soup.find(name="span", class_="a-price-fraction")

price = price_dollars.text + price_cents.text
price_float = float(price)

product_name = soup.find(name="span", id="productTitle")
product_name = product_name.text
product_name = product_name.strip()

if price_float < TARGET_PRICE:
    message = f"{product_name} is now ${price}, buy now!\n{URL}"
    message = message.encode("utf-8")
    # message = unidecode(message)
    print(message)
    print(type(message))
    my_email = "nmsparkles@gmail.com"
    password = "tqbh bgpz kboa lenq"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Amazon Deal!\n\n {message.decode('utf-8')}")
