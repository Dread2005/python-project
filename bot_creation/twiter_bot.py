import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Chrome_options = webdriver.ChromeOptions()
rain_download = 70
rain_upload = 30

class twitter:
    def __init__(self):
        Chrome_options.add_experimental_option("detach", True)
        self.down = 100
        self.up = 44.0
        self.twitter_email = "tshifhiwachedzafordjr@gmail.com"
        self.twitter_password = "76102005"
        self.twitter_username = "fewhoursman"
        self.Chrome_webdriver = webdriver.Chrome(Chrome_options)

    def twitter_bot(self):
        self.Chrome_webdriver.get("https://x.com/messages/862558006134923264-1355143022598610944")#https://x.com/i/flow/login")
        time.sleep(7)

        sign_in_email = self.Chrome_webdriver.find_element(By.NAME, 'text')
        sign_in_email.send_keys(self.twitter_email, Keys.ENTER)

        time.sleep(90)
        try:

            time.sleep(5)
            password = self.Chrome_webdriver.find_element(By.NAME, "password")
            password.send_keys(self.twitter_password, Keys.ENTER)

        except NoSuchElementException:

            time.sleep(5)
            username = self.Chrome_webdriver.find_element(By.NAME, 'text')
            username.send_keys(self.twitter_username, Keys.ENTER)
            time.sleep(5)
            password = self.Chrome_webdriver.find_element(By.NAME, "password")
            password.send_keys(self.twitter_password, Keys.ENTER)
        time.sleep(6)
        # msg_box = self.Chrome_webdriver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div/div/div[2]/div/div/aside/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
        # msg_box.send_keys("My rain upload and download speed is low", Keys.ENTER)

    def data_checker(self):
        self.Chrome_webdriver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.Chrome_webdriver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        go_button = self.Chrome_webdriver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()
        time.sleep(60)
        download = self.Chrome_webdriver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload = self.Chrome_webdriver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        if rain_upload > float(upload) and rain_download > float(download):
            self.twitter_bot()
        elif rain_upload > float(upload):
            self.twitter_bot()
        elif rain_download > float(upload):
            self.twitter_bot()

t_bot = twitter()
#t_bot.twitter_bot()
t_bot.data_checker()
