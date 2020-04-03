# Name:         test_01_login.py
# Description:  python作业
# Author:       python23_年华
# Date:         2019/12/30 20:09


# from ddt import ddt, data
# import unittest
import pytest
import time
from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from TestDatas import login_datas as LD


@pytest.fixture
def login_pre_post(login_pre_post_comm):
    login = LoginPage(login_pre_post_comm)
    yield login_pre_post_comm, login


@pytest.mark.usefixtures("login_pre_post")
class TestLogin:

    # 登录成功
    @pytest.mark.smoke
    def test_01_login_success(self, login_pre_post):
        # 登录操作
        login_pre_post[1].to_login(LD.success_datas["phone"], LD.success_datas["password"])
        time.sleep(2)
        # 断言
        # 如果登录成功，url会变
        assert (login_pre_post[0].current_url == LD.success_datas["chek_url"]) is True
        # 登录成功  可以找到"我的账户"
        assert (HomePage(login_pre_post[0]).judge_login_status())

    # 登录失败
    # pytest的数据驱动实现形式
    @pytest.mark.parametrize('case', LD.wrong_datas)
    def test_02_login_fail(self, case, login_pre_post):
        # 设置标志位，把提示区别开
        if case['case_id'] <= 5:
            flag = True
        else:
            flag = False
            # 登录操作
        login_pre_post[1].to_login(case['phone'], case['password'])
        time.sleep(2)
        # 判断提示的错误信息是否一致
        assert (login_pre_post[1].alert_error_msg(flag) == case['check']) is True
