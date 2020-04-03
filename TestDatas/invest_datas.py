# Name:         invest_datas.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/4 12:31


# 正常投资用例
success_datas = {'money': 5000}

# 投资失败 投标按钮不可点击 投资金额不是10的整数倍
fail_datas_one = [
    {"money": 123, "check": "请输入10的整数倍"},
    {"money": -12, "check": "请输入10的整数倍"},
    {"money": 'a', "check": "请输入10的整数倍"},
    {"money": '￥', "check": "请输入10的整数倍"},
    {"money": '100.25', "check": "请输入10的整数倍"},
    {"money": '300a', "check": "请输入10的整数倍"}
]

# 投资失败 投标按钮可点击
fail_datas_two = [
    {"money": 0, "check": "请正确填写投标金额"},
    {"money": -200, "check": "请正确填写投标金额"},
    {"money": ' ', "check": "请正确填写投标金额"},
    {"money": 80, "check": "投标金额必须为100的倍数"}
]
