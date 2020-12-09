# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569
from Base.base import Base
# from Common.log import log
from selenium.webdriver.common.by import By
import time


class OrderPage(Base):
    # 用户名
    def detail_user_name(self):
        return self.findele(By.XPATH, '//*[@id="inputPassengerVue"]/div[1]/ul/li[2]/input')

    # 身份证号
    def detail_id_card(self):
        return self.findele(By.XPATH, '//*[@id="inputPassengerVue"]/div[1]/ul/li[3]/input')

    # 手机号
    def detail_phone(self):
        return self.findele(By.XPATH, '//*[@id="inputPassengerVue"]/div[1]/ul/li[6]/input')

    # content
    def detail_content(self):
        return self.findele(By.XPATH, '//*[@id="contact-mobile"]')

    def order_btn(self):
        return self.findele(By.XPATH, '//*[@id="bookButtonVue"]/button[1]')

    def user_info(self, name, idcard, phone):
        self.detail_user_name().send_keys(name)
        time.sleep(3)
        self.detail_id_card().send_keys(idcard)
        time.sleep(3)
        self.detail_phone().send_keys(phone)
        time.sleep(3)
        self.detail_content().send_keys(phone)
        time.sleep(10)
        self.order_btn().click()
        time.sleep(10)
        return self.url()
