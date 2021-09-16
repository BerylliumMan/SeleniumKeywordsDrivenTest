# -*- coding: utf-8 -*-
from RunTest.RunCases import runCase

"""
loginMode: 0,执行一个用例后关闭浏览器并重新打开,需要登录的产品在RunCases.py第46行后加入单独写的登录操作
           1,执行一个用例后回到首页
driver: other，无需登录的产品填写ohter,需要登录的产品可自行添加driver
testVersion: 测试版本号
testAPI: ip地址
testName: 项目名称
filename: 测试用例文件
index: 执行完一条用例后回到的页面
"""

loginMode = 1
driver = 'other'
testVersion = 'v1.1.0'
testAPI = 'https://www.baidu.com'
testName = 'FW'
filename = './Cases/testCases_fw.xlsx'
index = 'https://www.baidu.com'  # 执行完一条用例后回到首页

runCase().test_Case(
                    loginMode=loginMode,
                    driver=driver,
                    testVersion=testVersion,
                    testAPI=testAPI,
                    testName=testName,
                    filename=filename,
                    index=index
                    )
