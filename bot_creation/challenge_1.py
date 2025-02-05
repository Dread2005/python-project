from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

Up_coming_events_title = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/h2')
events = driver.find_elements(By.CSS_SELECTOR,".event-widget ul li a") #"div.medium-widget.event-widget.last > div > ul > li > a")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time") #"div.medium-widget.event-
event = {}
# event_1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# event_2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a')
# event_3 = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/a')
# event_4 = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/a')
# event_5 = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/a')
print(f"{Up_coming_events_title.text}:")
for n in range(len(event_times)):
    event[n] = {
        "time": event_times[n].text,
        "name": events[n].text
    }
print(f"{event}")
# for n in events:
#     event = n.text
#     print(event)



driver.quit()
