from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

webdriver = webdriver.Chrome(options=chrom_options)
webdriver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = webdriver.find_element(By.NAME, "fName")
first_name.send_keys("chiyedza", Keys.ENTER)

last_name = webdriver.find_element(By.NAME, "lName")
last_name.send_keys("ford", Keys.ENTER)

email_address = webdriver.find_element(By.NAME, "email")
email_address.send_keys("tshifhiwachedzafordjr@gmail.com")

button = webdriver.find_element(By.CSS_SELECTOR, "body  form  button")
button.click()

