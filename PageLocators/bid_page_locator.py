# Name:         bid_page_locator.py
# Description:  python作业
# Author:       python23_年华
# Date:         2020/1/4 10:55
from selenium.webdriver.common.by import By


class BidPageLocators:
    # 可在直接在首页中获取第一个标，也可采用这种进入标里面获取第一个标
    # 主页上的"投标"元素
    bid_element = (By.XPATH, '//a[text()="投标"]')
    # 标页面  确定当前页面的排在第一个的标
    bid_element_first = (By.XPATH, '//div[@id="per"]/following-sibling::div[1]//div[@class="title"]]')


