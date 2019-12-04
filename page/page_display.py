#使用alt+enter 快速导入模块
from selenium.webdriver.common.by import By

from base.base_init import Base_Init
from base.base_action import Base_Action

class Display_Page(Base_Action):
    #By.XPATH等可以通过webdriver类中查find_element方法
    display_button = By.XPATH,"//*[@text='Display']"
    search_button = By.XPATH,"//*[@content-desc='Search']"
    input_text_area = By.CLASS_NAME,"android.widget.EditText"
    back_button = By.CLASS_NAME,"android.widget.ImageButton"
    def display_click(self):
        # 调用base_action中的方法,使用点击方法就可以实现查找元素并点击
        self.click_test(self.display_button)
    def display_search(self):
        self.click_test(self.search_button)
    def display_input(self,keys):
        self.input_text_test(self.input_text_area,keys)
    def display_back_click(self):
        self.click_test(self.back_button)
