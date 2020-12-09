# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569
from Common.log import log
from selenium import webdriver


# 对base代码进行优化，增加
class Base:
    def __init__(self, driver):
        self.driver = driver

    # 单星号参数代表此处接收任意多个非关键词参数
    def findele(self, *args):
        try:
            print(args)
            log("通过" + args[0] + "定位，元素是" + args[1])
            return self.driver.find_element(*args)
        except:
            # 在页面上没有定位到相应的元素
            log("定位元素失败！")

    # 对元素 click
    def click(self, args):
        self.findele(args).click()

    # 输入值
    def sendkey(self, args, value):
        self.findele(args).send_keys(value)

    # 调用js
    def js(self, str):
        self.driver.execute_script(str)

    def url(self):
        return self.driver.current_url

    # 后退
    def back(self):
        self.driver.back()

    # 前进
    def forword(self):
        self.driver.forward()

    # 退出
    def quit(self):
        self.driver.quit()
