# Name:         user_page.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/4 16:39
from Common.basepage import BasePage
from PageLocators.user_page_locator import UserPageLocator as loc


class UserPage(BasePage):

    def get_user_available_balance(self):
        return self.get_element_text(loc.user_available_balance, "个人中心_获得可用余额").strip("元")
