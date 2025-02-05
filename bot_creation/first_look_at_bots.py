from selenium import webdriver
from selenium.webdriver.common.by import By
#keeping Chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#create a bridge:
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.co.za/Volkano-Bluetooth-Headphones-Hands-Free-Compatible/dp/B07H8L9RDZ?ref_=Oct_d"
           "_obs_d_28034761031_3&pd_rd_w=AbXpG&content-id=amzn1.sym.2abdd2d5-c466-424f-ab98-7f9c6148446d&pf_rd"
           "_p=2abdd2d5-c466-424f-ab98-7f9c6148446d&pf_rd_r=ZT2TYDRP28HFA5DBFMJ0&pd_rd_wg=De7fR&pd_rd_r=5f760322-"
           "68c4-453d-8d66-886f6bec604c&pd_rd_i=B07H8L9RDZ")

### Webscraping in Selenium ###
## Locator Strategies ##
#first import the By class(from selenium.webdriver.common.by import By)

#finding by Class:
price_rand = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")

#finding by Name:
search_bar = driver.find_element(By.NAME, "field-keywords")

#finding by Id
home_button = driver.find_element(By.ID, "nav-logo-sprites")
brand_link = driver.find_element(By.ID, "bylineInfo")

#finding by CSS_Selector:
    #Css_Selector_example = driver.find_element(By.CSS_SELECTOR, ".a-section a-spacing-none a") # ".a-section a-spacing-none" is the class and "a" is the element you are looking for in the first element with the class

#finding by Xpath
#go to inspect, copy, copy Xpath, use single quotes '' paste Xpath between single quotes
in_stock = driver.find_element(By.XPATH, '//*[@id="availability"]/span')


#".close" just closes the active tab
#driver.close()

#".quit" closes the entire browser
#driver.quit()

print(f"price = {price_rand.text}.{price_cents.text}")
print(search_bar.get_attribute("placeholder"))
print(f"Size = {home_button.size}")
print(brand_link.get_attribute("href"))
print(in_stock.text)

driver.quit()
