import requests
import smtplib
import json
from bs4 import BeautifulSoup

with open('./day_41-50/day_47/creds.json') as file:
    creds = json.load(file)

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
}

url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

response = requests.get(url=url, headers = headers)
soup = BeautifulSoup(response.text, 'lxml')

price = soup.find("span", id = "priceblock_ourprice").get_text()
price_no_currency = price.split("$")[1]
price = float(price_no_currency)
title = soup.find(id="productTitle").get_text().strip()

print(price)

BUY_PRICE = 200

if price < BUY_PRICE:
    message =f"Your item {title} is now within your buy price of {BUY_PRICE}, please proceed to {url} to make purchase"
    print (message)
    # with smtplib.SMTP('smtp.gmail.com') as connection:
    #     connection.starttls()
    #     connection.login(creds['email'], creds['password'])
    #     connection.sendmail(
    #         from_addr=creds['email'],
    #         to_addrs=creds['destination'],
    #         msg=f"Subject: Amazon Prize Alert!\nYour item {title} is now within your buy price of {BUY_PRICE}, please proceed to {url} to make purchase"
    #     )