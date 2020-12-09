# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569
import unittest
from  selenium import webdriver
from Common.function import config_url
# 抽离单元测试中的setUp和tearDown
class UnitBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    def tearDownClass(cls) -> None:
        cls.driver.quit()

