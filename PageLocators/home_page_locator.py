# Name:         home_page_locators.py
# Description:  python作业
# Author:       python23_年华
# Date:         2019/12/30 20:14

from selenium.webdriver.common.by import By


# 可在直接在首页中获取第一个标，也可采用进入标页面里获取第一个标
class HomePageLocators:
    # 我的账户
    element_my_account = (By.XPATH, '//a[contains(text(),"我的帐户")]')

    # 获取首页中，排在第一位的标
    element_first_bid = (By.XPATH, '//div[@class="b-unit-list clearfix"]/div[1]//div[@class="b-title"]')
