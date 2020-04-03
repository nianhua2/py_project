# Name:         test_02_invest.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/4 16:12

import pytest
from PageObjects.user_page import UserPage
from TestDatas import invest_datas as ID
from PageObjects.home_page import HomePage
from PageObjects.invest_page import InvestPage


@pytest.fixture
def invest_pre_post(invest_pre_post_comm):
    HomePage(invest_pre_post_comm).click_first_bid()
    invest = InvestPage(invest_pre_post_comm)
    yield invest_pre_post_comm, invest


@pytest.mark.usefixtures("invest_pre_post")
class TestInvest:

    
    def test_01_success_invest(self, invest_pre_post):
        # 获取标的借款金额
        loan_amount = invest_pre_post[1].get_loan_amount()
        # 获取剩余金额
        surplus_amount_before = float(invest_pre_post[1].get_surplus_amount())
        # 获取用户账户余额
        user_amount_before = float(invest_pre_post[1].get_user_amount())
        # 输入投资金额
        invest_pre_post[1].input_loan_amount(ID.success_datas['money'])
        # 点击投标按钮
        invest_pre_post[1].click_invest_button()
        # 出现投资成功的弹窗,点 查看激活
        invest_pre_post[1].click_invest_success_alert()
        # 获取个人中心中的账户余额
        user_amount = float(UserPage(invest_pre_post[0]).get_user_available_balance())
        # 回退上上一网页
        invest_pre_post[0].back()
        # 刷新网页
        invest_pre_post[0].refresh()
        # 获取标剩余金额
        surplus_amount_after = float(invest_pre_post[1].get_surplus_amount())
        # 断言   投资的金额 = 剩余金额前-剩余金额后 = 用户金额前 -用户金额后
        assert (ID.success_datas['money'] == int((surplus_amount_before - surplus_amount_after) * 10000)) is True
        assert (ID.success_datas['money'] == int(user_amount_before - user_amount)) is True

    @pytest.mark.parametrize('case', ID.fail_datas_one)
    def test_02_fail_invest_one(self, case, invest_pre_post):
        # 获取剩余金额
        surplus_amount_before = float(invest_pre_post[1].get_surplus_amount())
        # 获取用户账户余额
        user_amount_before = invest_pre_post[1].get_user_amount()
        # 输入投资金额
        invest_pre_post[1].input_loan_amount(case['money'])
        # 获取失败的提示信息
        error_msg_from_button = invest_pre_post[1].get_error_msg_from_button()
        # 刷新网页
        invest_pre_post[0].refresh()
        # 获取标剩余金额
        surplus_amount_after = float(invest_pre_post[1].get_surplus_amount())
        # 获取用户账户余额
        user_amount_after = invest_pre_post[1].get_user_amount()
        # 投资按钮不可点击， 但输入的金额不合法或者不是10的倍数，错误提示直接展示在按钮上
        # 断言 提示信息
        assert (case['check'] == error_msg_from_button) is True
        # 断言  标余额未变
        assert (surplus_amount_after == surplus_amount_before) is True
        # 断言  账户余额未变
        assert (user_amount_before == user_amount_after) is True

    @pytest.mark.parametrize('case', ID.fail_datas_two)
    def test_03_fail_invest_two(self, case, invest_pre_post):
        # 获取剩余金额
        surplus_amount_before = float(invest_pre_post[1].get_surplus_amount())
        # 获取用户账户余额
        user_amount_before = invest_pre_post[1].get_user_amount()
        # 输入投资金额
        invest_pre_post[1].input_loan_amount(case['money'])
        # 点击投标按钮
        invest_pre_post[1].click_invest_button()
        # 获取失败的提示信息
        error_msg_from_alert = invest_pre_post[1].get_error_msg_from_alert()
        # 刷新网页
        invest_pre_post[0].refresh()
        # 获取标剩余金额
        surplus_amount_after = float(invest_pre_post[1].get_surplus_amount())
        # 获取用户账户余额
        user_amount_after = invest_pre_post[1].get_user_amount()
        # 投资按钮可点击  但输入的金额不是100的整数倍，或是是负数，或0
        # 断言 提示信息
        assert (case['check'] == error_msg_from_alert) is True
        # 断言  标余额未变
        assert (surplus_amount_after == surplus_amount_before) is True
        # 断言  账户余额未变
        assert (user_amount_before == user_amount_after) is True
