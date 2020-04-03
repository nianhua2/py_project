# Name:         invest_page_locator.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/4 11:22
from selenium.webdriver.common.by import By


class InvestPageLocator:
    # 标的借款金额
    invest_bid_loan_amount = (By.XPATH, '//span[@class="mo_span2"]')
    # 标的剩余金额
    invest_bid_surplus_amount = (By.XPATH, '//span[@class="mo_span4"]')
    # 投标页面  输入投资金额的输入框
    # invest_input_amount = (By.XPATH, '//div[@class="clearfix left"]')
    invest_input_amount = (By.XPATH, '//input[contains(@class,"invest-unit-investinput")]')
    # "群主特权“元素可见
    invest_element_visible = (By.XPATH,'//div[@class="footer"]/div[@class="left tt"]')
    # 全投
    invest_set_all = (By.XPATH, '//input[@class="set-all"]')
    # 投标
    invest_click_bid = (By.XPATH, '// button[@class="btn btn-special height_style"]')
    # 投标成功后的 关闭激活弹窗
    invest_click_success_alert = (By.XPATH,'//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投标失败 投标按钮点击后的失败提示
    invest_after_click_msg = (By.XPATH, '//div[@class="text-center"]')

