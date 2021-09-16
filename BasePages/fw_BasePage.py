# -*- coding: utf-8 -*-
"""
防火墙登录
"""

import time
from selenium import webdriver
from BasePages.getVerifyCode import fw_get_pictures

class FWlogin:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        time.sleep(2)

    def setDriver(self, testAPI):
        # noinspection PyBroadException

        try:
            self.driver.get(testAPI)
            self.driver.find_element('xpath', "//input[@placeholder='用户名']").send_keys('admin')
            self.driver.find_element('xpath', "//input[@placeholder='登录密码']").send_keys('admin@123')
            self.driver.find_element('xpath', "//input[@placeholder='验证码']").send_keys(fw_get_pictures(
                self.driver, 'xpath', "//img[@class='ng-star-inserted']"))
            self.driver.find_element('xpath', "//button[@class='login-form-button ant-btn ant-btn-primary']").click()
            time.sleep(3)
            assert '设备概况' == self.driver.find_element('xpath',
                                                      "//ul[@class='first-submenu ant-menu ant-menu-root ant-menu-"
                                                      "dark ant-menu-vertical']//li[1]//span[1]").text
            # return self.driver

        except Exception as e:
            print(e)
            time.sleep(2)
            self.setDriver(testAPI)
        finally:
            return self.driver
            

