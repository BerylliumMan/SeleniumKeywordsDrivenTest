# -*- coding: utf-8 -*-
"""
测试结果生成JSON
"""

import json


def write(FIELDS):
    with open("./Report/ResultJson/jsonFile.json", "w+", encoding='utf-8') as jsonFile:
        jsonFile.write(json.dumps(FIELDS, ensure_ascii=False, indent=4))
