# Name:         login_page_locators.py
# Description:  python作业
# Author:       python23_年华
# Date:         2019/12/30 20:10
from selenium.webdriver.common.by import By


class LoginPageLocators:
    # 手机号
    input_phone = (By.XPATH, '//input[@name="phone"]')
    # 密码
    input_password = (By.XPATH, '//input[@name="password"]')
    # 登录
    click_login = (By.XPATH, '//button[@type="button"]')
    # 基本错误提示信息  前端控制
    error_msg_from_front = (By.XPATH, '//div[@class="form-error-info"]')
    # 账号或密码错误 后端控制
    error_msg_from_back = (By.XPATH, '//div[@class="layui-layer-content"]')
