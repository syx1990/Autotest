# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569
import unittest
import time
from Common.function import project_path
from TestCases.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    test_dir = project_path() + "TestCases"
    tests = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = project_path() + "/Reports/" + now + '.html'
    fp = open(filepath, 'wb')
    # 定义测试报告的标题与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description='测试报告')
    runner.run(tests)
    fp.close()
