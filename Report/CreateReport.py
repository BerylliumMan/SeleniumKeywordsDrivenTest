# -*- coding: utf-8 -*-

import json
import os
import time


class BeautifulReport:

    def __init__(self):
        self.title = '测试报告'
        self.filename = 'report.html'
        self.FIELDS = None

    def set_fields(self, fileds):
        self.FIELDS = fileds

    def report(
            self,
            description,
            filename,
            log_path,
            report_temp):
        """
        生成测试报告,并放在当前运行路径下
        :param log_path: 生成report的文件存储路径
        :param filename: 生成文件的filename
        :param description: 生成文件的注释
        :return:
        """
        if filename:
            self.filename = filename if filename.endswith(
                '.html') else filename + '.html'

        if description:
            self.title = description

        self.log_path = os.path.abspath(log_path)

        self.output_report(report_temp)

    # 运行一个suit重写一次
    def output_report(self, template_path):
        """
        生成测试报告到指定路径下
        :return:
        """
        override_path = os.path.abspath(self.log_path) if \
            os.path.abspath(self.log_path).endswith('/') else \
            os.path.abspath(self.log_path) + '/'

        with open(template_path, 'rb') as file:
            body = file.readlines()
        file.close()
        file = (override_path + self.filename).replace("\\", "/")
        # print(file)
        with open(file, 'wb') as write_file:
            for item in body:
                if item.strip().startswith(b'var resultData'):
                    head = '    var resultData = '
                    item = item.decode().split(head)
                    item[1] = head + json.dumps(self.FIELDS, ensure_ascii=False, indent=4)
                    item = ''.join(item).encode()
                    item = bytes(item) + b';\n'
                write_file.write(item)
            write_file.close()


class get_report:

    def make_report(self):
        # 获取当前文件所在的路径
        current_dir = os.path.abspath(os.path.dirname(__file__))

        # 拼接template模板文件所在的路径
        template_path = os.path.join(current_dir, 'Templates/template.html')
        # print('template_path = ', template_path)

        # HTML report 存放路径
        report_path = os.path.join(current_dir)

        # print('report_path = ', report_path)
        # 创建对象
        beautifulReport = BeautifulReport()
        with open("./Report/ResultJson/jsonFile.json", "r", encoding='utf-8') as f:
            FIELDS = json.load(f)
        beautifulReport.set_fields(FIELDS)
        # print('&&&&&& make report &&&&&&')
        reporttime = time.strftime("%Y-%m-%d_%H%M%S")
        beautifulReport.report(filename=f'Report_{reporttime}.html', description="test", log_path=report_path,
                               report_temp=template_path)
        # print('&&&&&& end &&&&&&')


if __name__ == '__main__':
    get_report().make_report()
