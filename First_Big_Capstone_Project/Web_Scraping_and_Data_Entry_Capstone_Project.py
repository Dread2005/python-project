import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import requests

#Form#
form = "https://forms.gle/phQefnHnPANPLeHJ6"

#driver
Chrome_oprtions = webdriver.ChromeOptions()
Chrome_oprtions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=Chrome_oprtions)
driver.get(form)

#soup
Zillow_link = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_txt = Zillow_link.text

soup = BeautifulSoup(zillow_txt, "html.parser")
proprty_links = soup.find_all(name="a", class_="property-card-link")
preoperty_price = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")

link_list = []
price_list = []

for text in preoperty_price:
    price = text.text
    price_list.append(price.split("+")[0].replace("/mo", "").strip())

    #price_list.append(price[])

for txt in proprty_links:
    links = txt.text
    a = txt.get("href")
    link_list.append(a)

#print(link_list)
#print(price_list)
list_length = len(price_list)

building_library = []

for n in range(list_length):
    building_library.append(f"{price_list[n]} - {link_list[n]}")
#print(building_library)
for n in range(len(building_library)):
    building_price = building_library[n].split("-")[0]
    building_link = building_library[n].split("-")[1]
    time.sleep(5)
    price_insert = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_insert = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_insert.send_keys(building_price)
    link_insert.send_keys(building_link, Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Submit another response").click()





