import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

CHROME_DRIVER_PATH = "./chromedriver.exe"
GOOGLE_FORMS = "https://docs.google.com/forms/d/e/1FAIpQLScuDNkRsoEssvwskACT-pfDprhTKVIk9yjTj_35XqWkZDUPUg/viewform?usp=sf_link"
URL_TO_SCRAPE = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
}

response = requests.get(url = URL_TO_SCRAPE, headers = headers)
soup = BeautifulSoup(response.text, "html.parser")
data = soup.find("ul", "photo-cards")
articles = data.find_all('article')

prop_price = [(article.find("ul", "list-card-details").text.split())[0] for article in articles]
prop_address = [article.find("address", "list-card-addr").text for article in articles]
prop_link = ["https://zillow.com" + article.find("a")['href'] for article in articles]

print (prop_address)
print (prop_price)
print (prop_link)


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

for n in range(len(prop_link)):
    driver.get(GOOGLE_FORMS)
    
    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    

    address.send_keys(prop_address[n])
    price.send_keys(prop_price[n])
    link.send_keys(prop_link[n])
    submit_button.click()