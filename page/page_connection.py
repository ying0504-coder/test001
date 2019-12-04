from selenium.webdriver.common.by import By

from base.base_init import Base_Init
from base.base_action import Base_Action

class Connection_Page(Base_Action):
    #定义页面要素的变量和定位方式
    more_button = By.XPATH,"//*[@text='More']"
    more_cellular_button = By.XPATH,"//*[@text='Cellular networks']"
    cellular_preferred_button = By.XPATH,"//*[@text='Preferred network type']"
    more_2g_button = By.XPATH,"//*[@text='2G']"
    more_3g_button = By.XPATH, "//*[@text='3G']"
    #定义页面各个操作的函数
    def connection_more_click(self):
        self.click_test(self.more_button)
    def connection_more_cellular_click(self):
        self.click_test(self.more_cellular_button)
    def connection_cellular_preferred_click(self):
        self.click_test(self.cellular_preferred_button)
    def connection_2g(self):
        self.click_test(self.more_2g_button)
    def connection_3g(self):
        self.click_test(self.more_3g_button)

