import time
from selenium import webdriver
from BasePages.getVerifyCode import get_pictures


class OhterPage:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        time.sleep(2)

    def get_driver(self, testAPI):
        self.driver.get(testAPI)
        return self.driver
