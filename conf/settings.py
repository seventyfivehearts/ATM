# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 14:47
# @Author  : sunzhen
# @File    : settings.py
# @Software: PyCharm
# 配置信息

import os
# 获取项目根目录路径
BASE_PATH = os.path.dirname(
    os.path.dirname(__file__))

# 获取user_data文件夹目录路径
USER_DATA_PATH = os.path.join(
    BASE_PATH, os.pardir
)
print(USER_DATA_PATH)
# D:\PycharmDemo\ATM\db\user_data
