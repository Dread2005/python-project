from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

### Login ###
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

linkedin_webdriver = webdriver.Chrome()
linkedin_webdriver.get("https://www.linkedin.com/jobs/?originalSubdomain=sa")

#enter email:
email = linkedin_webdriver.find_element(By.ID, "session_key")
email.send_keys("tshifhiwachedzafordjr@gmail.com", Keys.ENTER)

#enter password:
password = linkedin_webdriver.find_element(By.ID, "session_password")
password.send_keys("76102005", Keys.ENTER)

time.sleep(3)
search_job = linkedin_webdriver.find_element(By.CSS_SELECTOR, "#jobs-search-box-keyword-id-ember27")
search_job.send_keys("python developer", Keys.ENTER)

time.sleep(3)


search_city = linkedin_webdriver.find_element(By.CSS_SELECTOR, "#jobs-search-box-location-id-ember222")
search_job.send_keys("South Africa", Keys.ENTER)
time.sleep(60**2)
