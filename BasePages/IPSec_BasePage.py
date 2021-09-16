# -*- coding: utf-8 -*-
"""
IPSec VPN登录
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from BasePages.getVerifyCode import get_pictures


class IPSecLogin:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        time.sleep(2)

    def setDriver(self, testAPI):
        # noinspection PyBroadException
        self.driver.get(testAPI)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@placeholder='请输入管理员名']").send_keys('anquan')
        self.driver.find_element_by_xpath("//input[@placeholder='请输入登录密码']").send_keys('test2020+')
        self.inputcode()
        return self.driver

    def inputcode(self):
        try:
            code = get_pictures(self.driver, 'xpath', "//img[@id='imgVerify']")
            times = str(time.time()).replace(".", '')
            self.driver.find_element('xpath', "//input[@placeholder='请输入验证码']") \
                .send_keys(code)
            time.sleep(0.5)
            self.driver.find_element_by_id('login').click()
            exit = WebDriverWait(self.driver.find_element('link text', '退出'), 5, 0.5)
            # 保存识别正确的图片，用于训练模型
            os.rename('./BasePages/verifyCodePic/poo3.png', f'./BasePages/verifyCodePic2/{code}_{times}.png')
        except Exception as e:
            # print(e)
            os.rename('./BasePages/verifyCodePic/poo3.png', f'./BasePages/verifyCodePic2/{code}_{times}_需修改.png')
            self.inputcode()
