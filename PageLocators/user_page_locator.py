# Name:         user_page_locator.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/4 16:35
from selenium.webdriver.common.by import By


class UserPageLocator:
    # 可用余额
    user_available_balance = (By.XPATH, '//li[@class="color_sub"]')
