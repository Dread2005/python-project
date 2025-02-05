from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

job_list = []

### Login ###
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

Pnet_webdriver = webdriver.Chrome(options=chrome_options)
Pnet_webdriver.get("https://www.pnet.co.za/")
time.sleep(4)

#Accept:
Pnet_webdriver.find_element(By.ID, "ccmgt_explicit_accept").click()
time.sleep(3)

sign_in = Pnet_webdriver.find_elements(By.XPATH, '//*[@id="sub-menu-item"]')
for button in sign_in:
    button.click()

time.sleep(3)
signin_button = Pnet_webdriver.find_element(By.LINK_TEXT, "Sign in")
signin_button.click()

time.sleep(3)
email = Pnet_webdriver.find_element(By.CSS_SELECTOR, "#stepstone-form-element-19")
email.send_keys("Tshifhiwachedzafordjr@gmail.com")

time.sleep(3)
password = Pnet_webdriver.find_element(By.NAME, "password")
password.send_keys("76102005", Keys.ENTER)

time.sleep(3)
log_in_button = Pnet_webdriver.find_element(By.XPATH, '//*[@id="login-registration-dialog-1"]'
                                                      '/div/div[1]/div/div/div[1]/div[1]/div/div[6]'
                                                      '/div/div[1]/button')
log_in_button.click()

time.sleep(3)
job_search = Pnet_webdriver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div/input')
job_search.send_keys("Python Developer")

area_search = Pnet_webdriver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div/div/input')
area_search.send_keys("South Africa", Keys.ENTER)

time.sleep(3)

save_button = Pnet_webdriver.find_elements(By.CSS_SELECTOR, "div h2 a")
for n in save_button:
    job_list.append(n)

job_list[0].click()

job_windows = Pnet_webdriver.window_handles[1]
Pnet_webdriver.switch_to.window(job_windows)

time.sleep(3)
save = Pnet_webdriver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/'
                                             'article/div/div[2]/div[1]/div/ul/li[2]/button')
save.click()
Pnet_webdriver.quit()