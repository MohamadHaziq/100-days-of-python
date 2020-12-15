from selenium import webdriver
import time
import random

chrome_driver_path = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Cookie
cookie = driver.find_element_by_id('cookie')

# Store selector
store = driver.find_elements_by_css_selector('#store div')
item_id = [item.get_attribute("id") for item in store]
print (item_id)

timeout = time.time() + 5
game_time = time.time() + (60*5)

while True:
    cookie.click()
    if time.time() > timeout:

        # price in <b>
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # b to integer
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)

        # Get cost of upgrades
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_id[n]

        # How many cookies
        money_element = driver.find_element_by_id('money').text
        if "," in money_element:
            money_element = money_element.replace(",","")
        cookie_count = int(money_element)

        # Upgrade check
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id        

        # Purchase da best
        highest_upgrade = max(affordable_upgrades)
        purchase = affordable_upgrades[highest_upgrade]
        driver.find_element_by_id(purchase).click()

        time.sleep(1)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id        

        # Purchase da best
        try:
            highest_upgrade = max(affordable_upgrades)
            purchase = affordable_upgrades[highest_upgrade]
            driver.find_element_by_id(purchase).click()
        except:
            pass

        timeout = time.time() + random.randint(3, 10)

    if time.time() > game_time:
        cookie_per_s = driver.find_element_by_id("cps").text
        print (cookie_per_s)
        break
