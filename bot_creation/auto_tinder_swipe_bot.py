import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, ElementClickInterceptedException

playing = True
time_out = time.time() + 30

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_experimental_option("detach", True)

tinder_webdriver = webdriver.Chrome(options=Chrome_options)

tinder_webdriver.get("https://tinder.com/")

####windows that open from other windows:
#Base window:
tinder_window = tinder_webdriver.window_handles[0]
#Second window:

time.sleep(20)
login_button = tinder_webdriver.find_element(By.LINK_TEXT, 'Log in')
login_button.click()

time.sleep(3)
facebook_login = tinder_webdriver.find_element(By.CSS_SELECTOR, 'span div:nth-child(2) button')
facebook_login.click()

time.sleep(3)
#Changing and switching through windows:
fb_window = tinder_webdriver.window_handles[1]
tinder_webdriver.switch_to.window(fb_window)

face_book_email = tinder_webdriver.find_element(By.XPATH, '//*[@id="email"]')
face_book_email.send_keys("tshifhiwachedzafordjr@gmail.com", Keys.ENTER)

face_book_pass = tinder_webdriver.find_element(By.XPATH, '//*[@id="pass"]')
face_book_pass.send_keys("Tshifhiwa&76102005", Keys.ENTER)

tinder_webdriver.switch_to.window(tinder_window)

time.sleep(120)
tinder_webdriver.find_element(By.XPATH, '//*[@id="u-143730669"]/div/div[1]/div/div/div[3]/button[1]').click()

time.sleep(10)
tinder_webdriver.find_element(By.XPATH, '//*[@id="u-143730669"]/div/div[1]/div/div/div[3]/button[2]').click()

time.sleep(5)
tinder_webdriver.find_element(By.XPATH, '//*[@id="u-143730669"]/div/div[1]/div/div[3]/button[2]').click()

time.sleep(10)
tinder_webdriver.find_element(By.XPATH, '//*[@id="u1584650407"]/div/div[2]/div/div/div[1]/div[1]/button').click()

time.sleep(9)
like_button = tinder_webdriver.find_element(By.CSS_SELECTOR, ' div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-like-default\) > button')

try:
    while playing:
        like_button.click()

except ElementClickInterceptedException:
    time.sleep(3)
    tinder_webdriver.find_element(By.CSS_SELECTOR, "div > div.Pt\(12px\).Pb\(8px\).Px\(36px\)--ml.Px\(24px\) > button.c1p6lbu0.D\(b\).Mx\(a\)").click()
while playing:
    try:
        like_button.click()
    except ElementClickInterceptedException:
        time.sleep(4)








