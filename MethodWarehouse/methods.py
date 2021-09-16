# -*- coding: utf-8 -*-
"""
关键字仓库
"""
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class methodCage:
    """
    执行动作
    """
    #跳转到指定URL
    @classmethod
    def get_url(cls, driver, step):
        try:
            driver.get(step[1])
        except Exception as e:
            print(e)


    # 左键点击
    @classmethod
    def click(cls, driver, step):
        time.sleep(0.1)
        try:
            WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(step[1], step[2])).click()
        except Exception as e:
            print(step)
            print(e)
            return False

    # 输入
    @classmethod
    def input(cls, driver, step):
        time.sleep(0.3)
        try:
            WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(step[1], step[2])).send_keys(step[3])
            # driver.find_element(method, element).send_keys(value)
        except Exception as e:
            print(step)
            print(e)
            return False

    # 清空输入框
    @classmethod
    def clear(cls, driver, step):
        # print(step)
        time.sleep(0.3)
        try:
            ele = WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(step[1], step[2]))
            ele.clear()
        except Exception as e:
            print(step)
            print(e)
            return False

    # 下拉框选择文本
    @classmethod
    def select(cls, driver, step):
        time.sleep(0.3)
        try:
            obj = WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(step[1], step[2]))
            Select(obj).select_by_visible_text(step[3])
        except Exception as e:
            print(step)
            print(e)
            return False

    # 休眠时间
    @classmethod
    def sleep(cls, driver, step):
        try:
            if step[2] == 's':
                time.sleep(int(step[1]))
            elif step[2] == 'm':
                sleeptime = int(step[1]) * 60
                time.sleep(int(sleeptime))
        except Exception as e:
            print(step)
            print(e)
            return False

    # 切换到iframe
    @classmethod
    def switch_to_iframe(cls, driver, step):
        try:
            obj = WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(step[1], step[2]))
            driver.switch_to.frame(obj)
        except Exception as e:
            print(step)
            print(e)
            return False

    # 切换到父级iframe
    @classmethod
    def switch_to_parent_iframe(cls, driver, step):
        try:
            driver.switch_to.parent_frame()
        except Exception as e:
            print(step)
            print(e)
            return False

    # 切换回到主界面
    @classmethod
    def switch_to_default_content(cls, driver, step):
        try:
            driver.switch_to_default_content()
        except Exception as e:
            print(step)
            print(e)
            return False

    # 刷新页面
    @classmethod
    def refresh(cls, driver, step):
        try:
            driver.refresh()
        except Exception as e:
            print(step)
            print(e)
            return False

    # 发送键盘操作
    @classmethod
    def press_key(cls, driver, step):

        if step[1] == 'esc':
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        else:
            # 待添加
            pass

    # 发送鼠标左键操作
    @classmethod
    def mouse_click(cls, driver, step):
        try:
            obj = WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(step[1], step[2]))
            ActionChains(driver).click(obj).perform()
        except Exception as e:
            print(step)
            print(e)
            return False

    # 直接使用js操作，用于angular页面定位
    @classmethod
    def executeScript(cls, driver, step):
        try:
            print(step)
            driver.execute_script(f"{step[2]}.click()")
        except Exception as e:
            print(step)
            print(e)
            return False

    """
    断言动作
    """

    # 文字相等断言
    @classmethod
    def assert_equal(cls, driver, method, element, value=''):
        time.sleep(0.2)
        try:
            a = 0
            while a <= 3:
                text = WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method, element)).text
                if value == text:
                    return True
                else:
                    a += 1
                    time.sleep(1)
                    if a == 3:
                        print("text: " + text)
                        print("value: " + value)
                        return False

        except Exception as e:
            print(e)
            return False

    @classmethod
    def assert_not_equal(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            text = WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element)).text
            # print('text:', text)
            if value != text:
                return True
            else:
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
                print("text: " + text)
                print("value: " + value)
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
            print(e)

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
            return False

    # 元素不存在断言
    @classmethod
    def assert_not_displayed(cls, driver, method, element, value=''):
        time.sleep(0.3)
        try:
            if WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method, element).is_displayed()):
                print(1)
                return False
            else:
                print(2)
                return True
        except Exception as e:
            print(e)
            return True

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
            print(e)

    @classmethod
    def assert_not_enabled(cls, driver, method, element, value=''):
        try:
            WebDriverWait(driver, 8, 0.5).until(lambda driver: driver.find_element(method, element))
            if driver.find_element(method, element).is_enabled():
                return False
            else:
                return True
        except Exception as e:
            print(e)

    # 填写验证码,value填写为要验证码输入的元素地址,用空格隔开（如：xpath //input[@placeholder='验证码']）
    # @classmethod
    # def getverifycode(cls, driver, method, element, value=''):
    #     method1 = value.split(' ')[0]
    #     element1 = value.split(' ')[1]
    #     time.sleep(0.5)
    #     try:
    #         WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method1, element1))
    #         driver.find_element(method1, element1).send_keys(get_pictures(driver, method, element))
    #     except Exception as e:
    #         print(e)

    # 输入框的值相等断言
    @classmethod
    def input_asert_equal(cls, driver, method, element, value=''):
        time.sleep(0.2)
        try:
            a = 0
            while a <= 3:
                text = WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method, element)) \
                    .get_attribute("value")
                # print('test:', text)
                if value == text:
                    return True
                else:
                    a += 1
                    time.sleep(1)
                    if a == 3:
                        print("text: " + text)
                        print("value: " + value)
                        return False

        except Exception as e:
            print(e)
            return False

    # 输入框的值不相等断言
    @classmethod
    def input_asert_not_equal(cls, driver, method, element, value=''):
        time.sleep(0.2)
        try:
            a = 0
            while a <= 3:
                text = WebDriverWait(driver, 5, 0.5).until(lambda driver: driver.find_element(method, element)) \
                    .get_attribute("value")
                # print('test:', text)
                if value == text:
                    a += 1
                    time.sleep(0.5)
                    if a == 3:
                        return False
                else:
                    # print("text: " + text)
                    # print("value: " + value)
                    return True

        except Exception as e:
            print(e)
            return False
