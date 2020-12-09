# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569
from Base.base import Base
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from Common.function import date_n


class SearchPage(Base):

    # 出发地
    def search_leave(self):
        return self.findele(By.ID, "departCityName")

    # 到达地
    def search_arrive(self):
        return self.findele(By.ID, "arriveCityName")

    # 出发时间
    def search_date(self):
        return self.findele(By.ID, "departDate")

    # 检索
    def search_btn(self):
        return self.findele(By.XPATH, '//*[@id="searchBoxTemplete"]/div/div[1]/div[2]/div/input')

    # 当前的火车车次
    def search_current(self):
        return self.findele(By.XPATH, '/html/body/div[7]/div/div[5]/div[3]/div/div[1]/div[6]/div[1]/a')

    # selenium执行js代码
    def search_js(self, value):
        jsvalue = "document.getElementById(" + "'" + value + "'" + ").removeAttribute('readonly')"
        return self.js(jsvalue)

    def search_train(self, leave, arrive, driver):
        self.search_leave().send_keys(leave)
        time.sleep(7)
        self.search_arrive().send_keys(arrive)
        time.sleep(7)
        tomorrow = date_n(1)
        self.search_js("departDate")
        self.search_date().clear()
        self.search_date().send_keys(tomorrow)
        time.sleep(5)
        ActionChains(driver).move_by_offset(0, 0).click().perform()
        # # 原理是鼠标点击右键
        self.search_btn().click()
        time.sleep(2)
        return self.url()
