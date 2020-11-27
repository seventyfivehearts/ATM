# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 14:56
# @Author  : sunzhen
# @File    : start.py
# @Software: PyCharm

# 程序的入口

# 添加解释器的环境变量
import sys
import os
sys.path.append(
    os.path.dirname(__file__)
)

from core import src
if __name__ == '__main__':
    # 先执行用户视图层
    src.run()
