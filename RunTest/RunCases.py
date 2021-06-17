# -*- coding: utf-8 -*-
"""
执行用例
"""
import time

from BasePages.fw_BasePage import login
from MethodWarehouse.methods import methodCage
from Cases.getCases import get_Cases
from Report.ResultJson.WriteJson import write
from Report.CreateReport import get_report


class runCase:

    def get_driver(self, driver, testAPI):
        if driver == 'FW':
            self.driver = login().setDriver(testAPI)
        else:
            pass
        return self.driver

    def test_Case(self, loginMode, driver, testVersion, testAPI, testName, filename):
        beginTime = time.strftime("%Y-%m-%d %H:%M:%S")  # 启动时间
        time1 = time.time()
        if loginMode == 1:
            self.get_driver(driver, testAPI)
        cases = get_Cases(filename)
        testResultList = []
        testAll = 0  # 执行数量
        testpass = 0  # 通过次数
        query_total_count = len(cases)  # 测试总数
        testError = 0
        testSkip = 0
        for case in cases:
            if int(float(case[-1])) == 1:
                testAll += 1  # 测试总数
                # print('正在执行用例：' + case[2])
                startTime = time.time()
                testResult = {'CaseNo': int(float(case[0])), 'module': case[1], 'tittle': case[2]}
                if loginMode == 0:
                    self.driver = login().setDriver(testAPI)
                for step in case[3].split('\n'):  # 执行用例
                    if hasattr(methodCage, step.split(',')[0]):
                        getattr(methodCage, step.split(',')[0])(self.driver, step.split(',')[1], step.split(',')[2],
                                                                step.split(',')[-1])
                if hasattr(methodCage, case[4]):  # 断言
                    if getattr(methodCage, case[4])(self.driver, case[5], case[6], case[7]):
                        print('用例：' + case[0] + case[2] + '执行成功')
                        testpass += 1
                        testResult['status'] = 'Success'  # 执行状态
                        testResult['log'] = f"<a href=#>执行成功</a>"
                        if loginMode == 1:
                            self.driver.get(testAPI)
                    else:
                        print('用例：' + case[0] + case[2] + '执行失败')
                        testError += 1
                        testResult['status'] = 'Fail'  # 执行状态
                        picTime = time.strftime("%Y-%m-%d_%H%M%S")
                        self.driver.get_screenshot_as_file(f'./Report/FailedPictures/{case[2]}_{picTime}.png')
                        testResult['log'] = f"<a href=../Report/FailedPictures/{case[2]}_{picTime}.png>查看截图</a>"
                        if loginMode == 1:
                            self.driver.get(testAPI)
                testResult['spendTime'] = str(int(time.time() - startTime)) + 's'  # 用例执行时间
                if loginMode == 0:
                    self.driver.close()
            else:
                testSkip += 1
                testResult = {}
            if testResult != {}:
                testResultList.append(testResult)
        if loginMode == 1:
            self.driver.close()
        query_lable_percent = "%.2f%%" % (testAll / query_total_count * 100)
        FIELDS = {'testResult': testResultList, 'testPass': testpass, "testAll": testAll,
                  "testError": testError, "testSkip": testSkip, "beginTime": beginTime,
                  "totalTime": str(int(time.time() - time1)) + 's', 'query_total_count': query_total_count,
                  "query_lable_count": testAll, "query_lable_percent": query_lable_percent, "testVersion": testVersion,
                  "testAPI": testAPI, "testName": testName}
        write(FIELDS)
        get_report().make_report()
