'''
Created on 2018年3月15日
'''
from .find_page_elements import FindPageElements
class DealWithElements:
    '''
    classdocs
    '''


    def __init__(self, driver):
        '''
        Constructor
        '''
        self.__driver = driver
        self.__elementHandle = FindPageElements(self.__driver)
        
    def assignElement(self, search_str, value, etype="input", by="ID"):
        element=self.__elementHandle.findElements(by=by, search_str=search_str)
        if etype == "input" or etype == "textarea":
            element.send_keys(value)
        if etype == "select":
            element.find_element_by_css_selector("option[value='"+value+"']").click()
    