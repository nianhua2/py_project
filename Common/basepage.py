# Name:         basepage.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/3 18:49
import datetime
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common import my_logger
from Common.file_path import PICTURE_DIR


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_element_visible(self, locator, name_action, timeout=20, poll_frequency=0.5):
        '''
        :param locator: 元素定位，实际是个元祖
        :param name_action:页面名称_行为名称 截图文件的名称中的一部分 eg:首页_点击登录_202001003.png
        :param timeout:
        :param poll_frequency:
        :return:
        '''
        logging.info(f"{name_action}:等待{locator}元素可见")
        try:
            start_time = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_all_elements_located(locator))
        except:
            # 级别：Error   tracebak的信息完整的写入日志
            logging.exception("等待元素可见失败")
            # 保存操作失败的截图
            self.save_screenshot_to_picture(name_action)
            raise
        else:
            end_time = datetime.datetime.now()
            logging.info(f"等待结束  开始时间为{start_time},结束时间为{end_time},等待耗时时间是{end_time-start_time}")

    # 查找元素
    def get_element(self, locator, name_action):
        '''
        :param locator:
        :param name_action:
        :return: 返回一个元素对象
        '''
        logging.info(f"页面{name_action}: 查找{locator}元素")
        try:
            element = self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败")
            self.save_screenshot_to_picture(name_action)
            raise
        else:
            logging.info(f"成功找到{locator}元素")
            return element

    # 输入文本内容
    def input_text(self, locator, value, name_action,timeout=20, poll_frequency=0.5):
        # 等待元素可见
        self.wait_element_visible(locator, name_action,timeout,poll_frequency)
        # 在页面查找到元素
        element = self.get_element(locator, name_action)
        logging.info(f"在页面:{name_action}对元素{locator},输入内容为:{value}")
        try:
            # self.driver.execute_script("arguments[0].scrollIntoView(false);",element)
            element.send_keys(value)
        except:
            logging.exception(f"向页面{name_action}输入文本{value}失败")
            self.save_screenshot_to_picture(name_action)
            raise

    # 点击元素
    def click_element(self, locator, name_action):
        # 等待元素可见
        self.wait_element_visible(locator, name_action)
        # 在页面查找到元素
        element = self.get_element(locator, name_action)
        logging.info(f"在页面:{name_action}对元素{locator},进行点击操作")
        try:
            element.click()
        except:
            logging.exception(f"在页面{name_action},点击操作失败")
            self.save_screenshot_to_picture(name_action)
            raise

    # 获得元素的文本值
    def get_element_text(self, locator, name_action):
        # 等待元素可见
        self.wait_element_visible(locator, name_action)
        # 在页面查找到元素
        element = self.get_element(locator, name_action)
        logging.info(f"在页面:{name_action}获取元素{locator}的文本值")
        try:
            text = element.text
        except:
            logging.exception(f"在页面{name_action},获取文本值失败")
            self.save_screenshot_to_picture(name_action)
            raise
        else:
            logging.info(f"在页面{name_action},获取文本值为{text}")
            return text

    # 获取元素的属性值
    def get_element_attribute(self, locator, attribute, name_action):
        # 等待元素可见
        self.wait_element_visible(locator, name_action)
        # 在页面查找到元素
        element = self.get_element(locator, name_action)
        logging.info(f"在页面:{name_action}获取元素{locator}的属性{attribute}的值")
        try:
            attribute_value = element.get_attribute(attribute)
        except:
            logging.exception(f"在页面{name_action},获取元素{locator}的属性{attribute}值失败")
            self.save_screenshot_to_picture(name_action)
            raise
        else:
            logging.info(f"在页面{name_action},获取元素{locator}的属性{attribute}的值为{attribute_value}")
            return attribute_value

    # 判断页面中某个元素是否存在且可见
    # 元素存在于页面返回True  不存在返回False
    def judge_element_exist_visible(self, locator, name_action, timeout=20, poll_frequency=0.5):
        logging.info(f"在页面:{name_action}判断元素：{locator}是否存在且可见")
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_all_elements_located(locator))
        except:
            logging.exception(f"在{timeout}时间内，未找到元素{locator}")
            self.save_screenshot_to_picture(name_action)
            return False
        else:
            logging.info(f"在{timeout}时间内，找到了元素{locator}")
            return True

    # 移动到元素element对象的“底端”与当前窗口的“底部”对齐
    def move_element_to_visible(self):
        pass


    # 保存执行过程中的失败截图
    def save_screenshot_to_picture(self, name_action):
        '''
        :param name_action: 页面名称_行为名称 截图文件的名称中的一部分 eg:首页_点击登录_202001003.png
                            完整规则为 页面名称_行为名称_操作时间.png
        :return:
        '''
        # 获取当前操作时间
        optime = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
        # 得到保存文件的名称，带png后缀
        filename = PICTURE_DIR + f"/{name_action}_{optime}.png"
        try:
            self.driver.save_screenshot(filename)
        except:
            logging.exception("保存截图失败")
        else:
            logging.info(f"保存截图成功,路径为：{filename}")
