# Name:         invest_page.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/4 11:48
from Common.basepage import BasePage
from PageLocators.invest_page_locator import InvestPageLocator as loc


class InvestPage(BasePage):
    # 获取用户金额
    def get_user_amount(self):
        return self.get_element_attribute(loc.invest_input_amount, "data-amount", "投标页面_获取用户的金额")

    # 获取借款金额
    def get_loan_amount(self):
        return self.get_element_text(loc.invest_bid_loan_amount,"投标页面_获取借款金额")

    # 获取标的剩余金额
    def get_surplus_amount(self):
        return self.get_element_text(loc.invest_bid_surplus_amount,"投标页面_获取借款剩余金额")

    # 输入投资金额
    def input_loan_amount(self,value):
        self.input_text(loc.invest_input_amount,value,"投标页面_输入投资金额")

    # 点击投标按钮
    def click_invest_button(self):
        self.wait_element_visible(loc.invest_element_visible,"投标页面_等待群主特权可见")
        self.click_element(loc.invest_click_bid,"投标页面_点击投标按钮")

    # 点击投标成功后的弹窗上的"查看激活"
    def click_invest_success_alert(self):
        self.click_element(loc.invest_click_success_alert,"投标页面_点击查看激活")

    # 获取页面错误提示信息，来自投标按钮
    def get_error_msg_from_button(self):
        return self.get_element_text(loc.invest_click_bid,"投标页面_获取按钮上错误信息")

    # 获取弹窗的错误提示信息
    def get_error_msg_from_alert(self):
        return self.get_element_text(loc.invest_after_click_msg,"投标页面_获取弹窗的错误信息")



