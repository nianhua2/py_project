# Name:         login_datas.py
# Description:  python作业
# Author:       python23_年华
# Date:         2019/12/30 20:27
from TestDatas.base_datas import home_url

# 登录成功的用例
success_datas = {
    "phone": "18684720553", "password": "python","chek_url":home_url
}


# 登录失败的用例
wrong_datas = [
        {"case_id": 1, "phone": "", "password": "python", "check": "请输入手机号"},
        {"case_id": 2, "phone": "18684720553", "password": "", "check": "请输入密码"},
        {"case_id": 3, "phone": "1868472055", "password": "python", "check": "请输入正确的手机号"},
        {"case_id": 4, "phone": "1868472055a", "password": "python", "check": "请输入正确的手机号"},
        {"case_id": 5, "phone": "186847205538", "password": "python", "check": "请输入正确的手机号"},
        {"case_id": 6, "phone": "18684720553", "password": "python299", "check": "帐号或密码错误!"}

    ]