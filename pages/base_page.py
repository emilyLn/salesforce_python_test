'''
Created on 2018年3月14日
'''
from utils.config import Config
from utils.config import CONFIG_FILE
from page_elements.deal_with_elements import DealWithElements
from page_elements.find_page_elements import FindPageElements
from selenium.common.exceptions import NoAlertPresentException

class BasePage:
    '''
    classdocs
    该类是页面元素及操作类的原始类
    定义从页面查找某元素，及为某个元素赋值的公共方法
    '''


    def __init__(self, driver,config_file_name=CONFIG_FILE):
        '''
        Constructor
                    定义私有变量：__driver: webdriver实例
                __config: Config类实例
                __element_list: 页面元素列表的配置信息
                __element_handle: 页面元素操作的公共类“DealWithElements”实例
                __element_finder: 页面元素获取的公共类“FindPageElements”实例
        '''
        self.__driver = driver
        self.__config = Config(config=config_file_name) #将配置文件类的实例放到self的数据空间中，此配置文件是调用时传入的，一般都是每个调用的功能页面对应的配置文件
        self.__element_handle = DealWithElements(driver)
        self.__element_finder = FindPageElements(driver)
        self.__project_config = Config(config=CONFIG_FILE) #专门用来取config.yml配置文件
        
    @property
    def driver(self):
        return self.__driver
    
    @property
    def config(self):
        return self.__config

    @property
    def element_handle(self):
        return self.__element_handle
    
    @property
    def element_finder(self):
        return self.__element_finder
    
    def getConfigInfo(self, element_name, *sub_elements):
        config_conf = self.__config.get(element_name)
        for sub_element in sub_elements:
            config_conf = config_conf.get(sub_element)
        return config_conf
            
    def findElement(self, element_name, *sub_elements):
        '''
                    得到页面的控件
        '''
        element_conf = self.getConfigInfo(element_name, *sub_elements)
        return self.element_finder.findElements(by=element_conf.get("by"), 
                            search_str=element_conf.get("search_str"))
    
    def findElementList(self, element_name, *sub_elements):
        '''
                    得到页面的控件列表
        '''
        element_conf = self.getConfigInfo(element_name, *sub_elements)
        return self.element_finder.findElementList(by=element_conf.get("by"), 
                            search_str=element_conf.get("search_str"))
        
    def assignElement(self, set_value, element_name, *sub_elements):
        '''
                    为页面的控件赋值
        '''
        element_conf = self.getConfigInfo(element_name, *sub_elements)
        self.element_handle.assignElement(by=element_conf.get("by"), 
                                          search_str=element_conf.get("search_str"), 
                                          etype=element_conf.get("type"), 
                                          value=set_value)
        
    def getLocator(self, element_name, *sub_elements):
        element_conf = self.getConfigInfo(element_name, *sub_elements)   
        locator = (self.__project_config.get(element_conf.get("by")), 
                element_conf.get("search_str"))
        return locator
    
    def catchPopupDialog(self):
        return self.__element_finder.getAlertPopup()
    
    def acceptAlert(self):
        self.catchPopupDialog().accept()
    
    def dismissAlert(self):
        self.catchPopupDialog().dismiss()