from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#
# wikidriver = webdriver.Chrome(options=chrome_options)
# take_driver = webdriver.Chrome(options=chrome_options)
#
# wikidriver.get("https://en.wikipedia.org/wiki/Main_Page")
# take_driver.get("https://www.takealot.com/")
#
# #art_count = wikidriver.find_element(By.CSS_SELECTOR, "#articlecount a")
# #art_count_number = art_count.text
#
# ###to click an item on a website###
# # #.click:
# #art_count.click()
#
# #find element by Link Text:
# all_portals = wikidriver.find_element(By.LINK_TEXT, "Content portals")
# #all_portals.click()
#
# ###typing on a website###
# search = take_driver.find_element(By.NAME, "search")
# #.send keys:
# #search.send_keys("Python")
#
# #sending keyboard inputs through Selenium:
# #First import keys: from selenium.webdriver.common.keys import Keys
# search.send_keys("Python", Keys.ENTER)
#
#
# wikidriver.quit()
# take_driver.quit()

app_brewery_drive = webdriver.Chrome(options=chrome_options)
app_brewery_drive.get("https://secure-retreat-92358.herokuapp.com/")

