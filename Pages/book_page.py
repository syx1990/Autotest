# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569

from Base.base import Base
from selenium.webdriver.common.by import By
from Common.log import log
import time


class BookPage(Base):

    # 预订车票
    def book(self):
        return self.findele(By.XPATH, '/html/body/div[7]/div/div[5]/div[3]/div/div[1]/div[6]/div[1]/a')

    def book_btn(self):
        try:
            time.sleep(10)
            self.book().click()
        except:
            log("车次查询失败")
            None
        time.sleep(10)
        return self.url()


