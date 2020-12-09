# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569
import os, configparser
import xlrd, os
from datetime import datetime, date, timedelta

# 获取项目路径
def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]


# 返回config.ini文件中testUrl
def config_url():
    config = configparser.ConfigParser()
    config.read(project_path() + "config.ini")
    return config.get('testUrl', 'url')

 # 时间
def date_n(n):
        return str((date.today() + timedelta(days=+int(n))).strftime("%Y-%m-%d"))


# 读取excel文件
def read_excel(filename, index):
    xls = xlrd.open_workbook(filename, encoding_override='utf-8')
    sheet = xls.sheet_by_index(index)
    # print(sheet.nrows)
    # print(sheet.ncols)
    dic = {}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
        dic[j] = data
    return dic


if __name__ == '__main__':
    # 读取Excel操作，返回字典
    data = read_excel(os.path.split(os.path.realpath(__file__))[0].split('C')[0] + "Data/testData.xlsx", 0)
    print(data)
    print(data.get(1))
    # print("项目路径为："+project_path())
    # print("被测试系统URL为："+config_url())
