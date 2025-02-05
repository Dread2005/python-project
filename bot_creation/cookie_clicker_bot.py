from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


playing = True
time_out = time.time() + 7
bot_clicker_timer = 60 * int(input("enter minutes: "))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://orteil.dashnet.org/experiments/cookie/")

# english_button = webdriver.find_element(By.LINK_TEXT, 'English')
# english_button.click()

#print(item_prices)

cookie_button = webdriver.find_element(By.ID, "cookie")

###the clicker###


while playing:

    cookie_button.click()

    if time.time() > time_out:
        items = webdriver.find_elements(By.CSS_SELECTOR, "#store div")
        item_ids = [item.get_attribute("id") for item in items]

        prices = webdriver.find_elements(By.CSS_SELECTOR, "#store b")
        cookie_num = webdriver.find_element(By.CSS_SELECTOR, "#money").text

        money = float(cookie_num)

        item_prices = []

        for price in prices:
            text_ = price.text
            if text_ != "":
                cost = float(text_.split(sep="-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        affordable_upgrades = {}

        for cost, ids in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = ids
                highest_price = max(affordable_upgrades)
                purchase_id = affordable_upgrades[highest_price]
                purchase = webdriver.find_element(By.ID, purchase_id)
                print(highest_price)
                print(purchase.text)
                purchase.click()
        time_out = time.time() + 5

if time.time() > bot_clicker_timer:
    playing = False







