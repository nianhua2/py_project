# Name:         home_page.py
# Description:  python作业
# Author:       python23_年华
# Date:         2019/12/30 20:08

from Common.basepage import BasePage
from PageLocators.home_page_locator import HomePageLocators as loc


# 继承BasePage类，获得其方法
class HomePage(BasePage):

    # 判断登录成功后，页面上有无"我的账户"元素出现
    def judge_login_status(self):
        return self.judge_element_exist_visible(loc.element_my_account, "主页_检查我的账户",10)

    # 点击进去第一个标
    def click_first_bid(self):
        self.click_element(loc.element_first_bid,"主页_点击第一个标")
