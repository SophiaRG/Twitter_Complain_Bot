from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
PROMISED_DOWN = 100
PROMISED_UP = 50
TWITTER_EMAIL = "Your email"
TWITTER_PASSWORD = "Your password"
TWITTER_USERNAME = "Your username"

class InternetSpeedTwitterBot :

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        #click start
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(50)

        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"down: {self.down}")
        print(f"up: {self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(5)
        email = self.driver.find_element(By.XPATH,
            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(3)
        try:
            password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys(TWITTER_USERNAME)
            username.send_keys(Keys.ENTER)
            time.sleep(3)
            password = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)

        time.sleep(3)

        input = self.driver.find_element(By.CSS_SELECTOR,'br[data-text="true"]')
        input.send_keys(f"My current internet speed is {self.down} Download and {self.up} Upload")
        time.sleep(3)
