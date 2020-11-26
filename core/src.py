# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 14:48
# @Author  : sunzhen
# @File    : src.py
# @Software: PyCharm
# 存放用户试图层
# 1.注册功能
def login():
    pass


# 2.登录功能
def register():
    username = input('请输入用户名：').strip()
    password = input('请输入密码：').strip()
    re_password = input('请确认密码：').strip()
    if password == re_password:
        # 1) 查看用户是否存在

        # 2) 若用户不存在，则保存用数据
        # 3) 若用户存在，则让用户从新输入
        user_dic = {
            'username': username,
            'password': password,
            'balance': 15000,
            'flow': [],
            # 用于记录用户购物车
            'shop_car': {},
            # locked:用于记录用户是否被冻结
            # False:未冻结
            'locked': False

        }
        import json
        import os
        from conf import settings
        # 用户数据
        with open('user_db.json', 'w', encoding='utf-8') as f:
            json.dump(user_dic, f)
        # 拼接用户的json文件路径

        user_path = os.path.join(
            settings.USER_DATA_PATH, f'{username}.json'
        )
        pass
    pass


# 3.查看余额
def check_balance():
    pass


# 4.提现功能
def withdraw():
    pass


# 5.还款功能
def repay():
    pass


# 6.转账功能
def transfer():
    pass


# 7.查看流水
def check_flow():
    pass


# 8.购物功能
def shopping():
    pass


# 9.查看购物车
def check_shop_car():
    pass


# 10.管理员功能
def admin():
    pass


# 创建函数主功能字典
func_dic = {
    '1': login,
    '2': register,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin
}


# 视图层主程序
def run():
    while True:
        print('''
        ===== ATM + 购物车 =====
        1.注册功能
        2.登录功能
        3.查看余额
        4.提现功能
        5.还款功能
        6.转账功能
        7.查看流水
        8.购物功能
        9.查看购物车
        10.管理员功能
        ======== end ======
        ''')

        choice = input('请输入功能编号：').strip()

        if choice not in func_dic:
            print('请输入正确的编号')
            continue
        func_dic.get(choice)()
