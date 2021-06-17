# -*- coding: utf-8 -*-
"""
关键字仓库
"""
import time
from selenium.webdriver.support.wait import WebDriverWait
from BasePages.getVerifyCode import get_pictures
from selenium.webdriver.support.select import Select

class methodCage:
    """
    执行动作
    """

    # 左键点击
    @classmethod
    def click(cls, driver, method, element, value=''):
        time.sleep(0.1)
        try:
            
            WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method, element)).click()
        except Exception as e:
            print(e)
            return False

    # 输入
    @classmethod
    def input(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method, element)).send_keys(value)
            # driver.find_element(method, element).send_keys(value)
        except Exception as e:
            print(e)
            return False

    # 清空输入框
    @classmethod
    def clear(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method, element)).clear()
        except Exception as e:
            print(e)
            return False

    #下拉框选择文本
    @classmethod
    def select(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            obj = WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method, element))
            Select(obj).select_by_visible_text(value)
        except Exception as e:
            print(e)
            return False

    @classmethod
    def sleep(cls, driver, sleeptime, timemode, value=''):
        try:
            if timemode == 's':
                time.sleep(int(sleeptime))
            elif timemode == 'm':
                sleeptime = int(sleeptime) * 60
                time.sleep(int(sleeptime))
        except Exception as e:
            print(e)
            return False


    """
    断言动作
    """

    # 文字相等断言
    @classmethod
    def assert_equal(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            text = WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element)).text
            if value == text:
                return True
            else:
                print("text: " + text)
                print("value: " + value)
                return False
        except Exception as e:
            print(e)
            return False

    # 文字包含断言
    @classmethod
    def assert_in(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            text = WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element)).text
            if value in text:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    # 选中断言
    @classmethod
    def assert_selected(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element))
            if driver.find_element(method, element).is_selected():
                return True
            else:
                return False
        except Exception as e:
            return e

    # 元素存在断言
    @classmethod
    def assert_displayed(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element))
            if driver.find_element(method, element).is_displayed():
                return True
            else:
                return False
        except Exception as e:
            print(e)

    # 元素不存在断言
    @classmethod
    def assert_not_displayed(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element))
            if driver.find_element(method, element).is_displayed():
                return False
            else:
                return True
        except Exception as e:
           pass

    # 可编辑状态断言
    @classmethod
    def assert_enabled(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            
            WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element))
            if driver.find_element(method, element).is_enabled():
                return True
            else:
                return False
        except Exception as e:
           pass

    @classmethod
    def assert_not_enabled(cls, driver, method, element, value=''):
        try:
            
            WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element))
            if driver.find_element(method, element).is_enabled():
                return False
            else:
                return True
        except Exception as e:
           pass

    # 填写验证码,value填写为要验证码输入的元素地址,用空格隔开（如：xpath //input[@placeholder='验证码']）
    @classmethod
    def getverifycode(cls, driver, method, element, value=''):
        method1 = value.split(' ')[0]
        element1 = value.split(' ')[1]
        time.sleep(0.5)
        try:
            WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method1, element1))
            driver.find_element(method1, element1).send_keys(get_pictures(driver, method, element))
        except Exception as e:
            print(e)


