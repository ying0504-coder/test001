import os,sys

import allure

sys.path.append(os.getcwd())
import pytest
from appium import webdriver
from base import base_init
from page.page_display import Display_Page
class Test_Display():

    def setup(self):
        self.driver = base_init.Base_Init()
        #将test在setup中创建的driver对象，通过page的init进行传递（一定是传递，不是重新调用init的方法）
        self.display_page = Display_Page(self.driver)

    @allure.step(title="测试步骤001")
    def test_display_search(self):
        self.display_page.display_click()
        self.display_page.display_search()
        allure.attach('描述', '我是测试步骤001的描述～～～')
        self.display_page.display_input("hello")
        self.display_page.display_back_click()
