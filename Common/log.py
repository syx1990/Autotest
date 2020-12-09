# -*- coding: utf-8 -*-
# !/usr/bin/python3
# author by : yuxiangShi
# tell  by: 18538187569
import logging, time
from Common.function import project_path


def log(str):
    # 创建一个handler,用于写入日志文件
    log_time = time.strftime("%Y_%m_%d_")
    # 路径需要修改
    log_path = project_path() + "/logs/"
    log_name = log_path + log_time + 'log.log'
    print(log_name)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s %(funcName)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=log_name,
                        filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)


if __name__ == '__main__':
    log("测试方案")
    log("212121")
