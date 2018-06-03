'''
Created on 2018年3月14日
'''
from selenium.webdriver.common.by import By
from utils.exceptions import CustmizeException
from utils.config import Config
from utils.config import CONFIG_FILE
from jmespath import search
from selenium.common.exceptions import NoAlertPresentException

class FindPageElements:
    '''
    classdocs
    '''

    def __init__(self, driver):
        '''
        Constructor
        '''
        self.__driver = driver
        self.__config = Config(config=CONFIG_FILE)
        
    def findElements(self, search_str="", by="ID"):
        if search_str == "":
            raise CustmizeException("The search string is null, can't find element.")
        
        by_model = self.__config.get(element=by)
        return self.__driver.find_element(by_model, search_str)
    
    def findElementList(self, search_str="", by="Name"):
        if search_str == "":
            raise CustmizeException("The search string is null, can't find element.")
        
        by_model = self.__config.get(element=by)
        return self.__driver.find_elements(by_model, search_str)
    
    def getAlertPopup(self): 
        '''
                        获得警告消息(Alert)：仅提供一个确认按钮让用户关系该消息，对应js的alert方法
                        确认消息(Confirm)：向用户提示一个是与否的问题，有确认和取消按钮，对应js的confirm方法
                        提示消息(Prompt)：提供一个文本字段，用户可以在其中输入一段文字，有确认和取消按钮，对应js的prompt方法
        '''
        try:
            alertDialog = self.__driver.switch_to.alert
        except NoAlertPresentException as e: 
            print("no alert")
        return alertDialog   