# Name:         conftest.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/6 16:13
import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import base_datas as BD


# 登录用例的前置后置
@pytest.fixture
def login_pre_post_comm():
    driver = webdriver.Chrome()
    # driver = webdriver.Ie()
    driver.maximize_window()
    driver.get(BD.login_url)
    # login = LoginPage(driver)
    yield driver
    driver.quit()


# 投资用例的前置后置
@pytest.fixture
def invest_pre_post_comm(login_pre_post_comm):
    # 关闭谷歌提示
    # option = webdriver.ChromeOptions()
    # option.add_experimental_option('useAutomationExtension', False)
    # option.add_experimental_option("excludeSwitches", ['enable-automation'])
    # self.driver = webdriver.Chrome(chrome_options=option)
    LoginPage(login_pre_post_comm).to_login(BD.user_phone, BD.user_password)
    # 点击首页中的第一个标
    # HomePage(login_pre_post).click_first_bid()
    # invest = InvestPage(login_pre_post)
    yield login_pre_post_comm
