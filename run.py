# -*- coding: utf-8 -*-
from RunTest.RunCases import runCase

"""
loginMode: 0,执行每个用例后关闭浏览器并重新打开
           1,执行所有用例只登录一次
driver: FW,防火墙
        非防护墙
testVersion: 测试版本号
testAPI：ip地址
testName：项目名称
filename :测试用例文件
"""

loginMode = 1  # 非防火墙项目请使用1，并自行添加用户登录用例
driver = 'FW'
testVersion = 'v1.1.0.3'
testAPI = 'https://192.168.11.178'
testName = '工业防火墙'
filename = './Cases/testCases.xlsx'

runCase().test_Case(
                    loginMode=loginMode,
                    driver=driver,
                    testVersion=testVersion,
                    testAPI=testAPI,
                    testName=testName,
                    filename=filename
                    )
