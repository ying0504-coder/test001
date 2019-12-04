import os,sys
sys.path.append(os.getcwd())
import pytest
from appium import webdriver
from base import base_init
from page.page_connection import Connection_Page

class Test_Connection():

    def setup(self):
        self.driver = base_init.Base_Init()
        self.connection_driver = Connection_Page(self.driver)
    def test_connection_2g(self):
        self.connection_driver.connection_more_click()
        self.connection_driver.connection_more_cellular_click()
        self.connection_driver.connection_cellular_preferred_click()
        self.connection_driver.connection_2g()
    def test_connection_3g(self):
        self.connection_driver.connection_more_click()
        self.connection_driver.connection_more_cellular_click()
        self.connection_driver.connection_cellular_preferred_click()
        self.connection_driver.connection_3g()

