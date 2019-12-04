from selenium.webdriver.support.wait import WebDriverWait

class Base_Action():
    def __init__(self, driver):
        self.driver = driver

    # 根据特征，对应的去找元素
    def find_element_test(self,location):
        location_by = location[0]
        location_path = location[1]
        #增加5秒等待超时，每1秒刷新一次
        return WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(location_by,location_path))

    #根据特征，对应的去找元素，并且点击
    def click_test(self,location):
        self.find_element_test(location).click()

    # 根据特征，对应的去找元素，并且输入文字
    def input_text_test(self,location,text):
        self.find_element_test(location).send_keys(text)

