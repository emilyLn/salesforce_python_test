'''
Created on 2018年3月20日
'''
import os
import time
from utils.config import Config
from utils.config import CONFIG_PATH
from utils.config import CONFIG_FILE
from utils.browser import Browser
from utils.exceptions import CustmizeException
from page_elements.element import Element
from page_elements.elements import Elements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.alert_dialog import AlertDialog
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from utils.log import logger

class Page:
    '''
    classdocs
    '''
    
    def __init__(self, page_name, file_suffix='yml'):
        '''
        Constructor
        '''
        self.__page_name = page_name
        self.__config_file = os.path.join(CONFIG_PATH, ".".join([page_name, file_suffix]))
        
        self.__config = Config(self.__config_file)
        self.__main_config = Config(CONFIG_FILE)
        if Browser.driver == None:
            raise CustmizeException("浏览器对象为空，不能操作页面")
        self.__driver = Browser.driver
    
    @property
    def page_name(self):
        return self.__page_name
    
    @property
    def driver(self):
        return self.__driver
    
    @property
    def main_config(self):
        return self.__main_config
    
    @property
    def by_mode(self):
        return self.__by_mode
    
    @property
    def search_str(self):
        return self.__search_str
    
    @property
    def tag(self):
        return self.__tag
    
    def getElementConfig(self,element_name, *sub_elements):
        config_file = self.__config.get(element_name)
        for element in sub_elements:
            config_file = config_file.get(element)
        self.__by_mode = config_file.get("method")
        self.__search_str = config_file.get("search_str")
        self.__tag = config_file.get("tag")
        
    def find_element(self):
        if self.__search_str == "":
            raise CustmizeException("The search string is null, can't find element.")
        try:
            element = self.__driver.find_element(self.__main_config.get(self.__by_mode), self.__search_str)
        except NoSuchElementException as e:
            e.trace_exception()
            logger.error("no such element: %s" % self.__search_str)
        return element
       
    def open(self, maximize_window=True):
        url = self.__config.get("URL")
        self.__driver.implicitly_wait(6)
        self.__driver.get(url)
        logger.info("open url = " + url)
        if maximize_window:
            self.__driver.maximize_window()
    #取单个元素
    def element(self, element_name, *sub_elements):
        logger.info("in page : %s get element : %s" % (self.__page_name, element_name))
        self.getElementConfig(element_name, *sub_elements)
        return Element(self.find_element(), self.__tag)
    #取列表元素
    def list(self, element_name, *sub_elements):
        self.loadWait(element_name)
        self.getElementConfig(element_name, *sub_elements)
        return Elements(driver = self.__driver, 
                       by = self.__main_config.get(self.__by_mode),
                       search_str = self.__search_str,
                       tag = self.__tag)
          
    def locator(self, element):
        self.getElementConfig(element)
        return (self.__main_config.get(self.__by_mode), self.__search_str)
    
    def loadWait(self, element):
        locator = self.locator(element)
        wait = WebDriverWait(self.__driver, 30)
        wait.until(expected_conditions.visibility_of_element_located(locator))
        
    def pageClose(self):
        self.__driver.close()
    
    def switchtoAlert(self):
        time.sleep(1)
        try:
            alertDialog = AlertDialog(self.__driver.switch_to.alert)
        except NoAlertPresentException as e: 
            print("no any alert dialog open")
        return alertDialog
    