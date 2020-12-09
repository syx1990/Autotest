# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569
import os
import sys

sys.path.append(os.path.split(os.getcwd())[0])
import time
import unittest
import HTMLTestRunner
from selenium import webdriver
from Common.function import read_excel, config_url, project_path
from Pages.search_page import SearchPage
from Pages.book_page import BookPage
from Pages.order_page import OrderPage


class logingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = read_excel(project_path() + "Data/testData.xlsx", 0)
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    def test_search_train(self):
        self.driver.get(config_url())
        search = SearchPage(self.driver)
        res = search.search_train(self.data.get(1)[1], self.data.get(1)[0], self.driver)
        # 本例断言是根据当前页面的URL来判断的
        self.assertIn('trainBooking', res)

    def test_book_page(self):
        book = BookPage(self.driver)
        res = book.book_btn()
        # 本例断言是根据当前页面的URL来判断的
        self.assertIn('inputPassengers', res)

    def test_order_page(self):
        order = OrderPage(self.driver)
        res = order.user_info("时玉祥", "412726199005045859", "18538187569")
        self.assertIn('orderDetail', res)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(logingTest("test_search_train"))
    suiteTest.addTest(logingTest("test_book_page"))
    suiteTest.addTest(logingTest("test_order_page"))

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath = project_path() + "/Reports/" + now + '.html'
    fp = open(filepath, 'wb')
    # 定义测试报告的标题与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description='测试报告')
    runner.run(suiteTest)
    fp.close()
