# Name:         login_page.py
# Description:  python作业
# Author:       python23_年华
# Date:         2019/12/30 20:07
from Common.basepage import BasePage
from PageLocators.login_page_locator import LoginPageLocators as loc


# 继承BasePage类，获得其方法
class LoginPage(BasePage):

    # 登录操作
    def to_login(self, phone, password):
        self.input_text(loc.input_phone, phone, "登录页面_输入手机号")
        self.input_text(loc.input_password, password, "登录页面_输入密码")
        self.click_element(loc.click_login, "登录页面_点击登录")

    # 登录失败的页面提示信息
    def alert_error_msg(self, flag=True):
        if flag:
            return self.get_element_text(loc.error_msg_from_front, "登录页面_获取前台校验的文本值")
        else:
            return self.get_element_text(loc.error_msg_from_back, "登录页面_获取后台校验的文本值")
