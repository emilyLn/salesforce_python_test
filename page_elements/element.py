'''
Created on 2018年3月21日
'''
from utils.exceptions import CustmizeException
from selenium.webdriver.support.select import Select

class Element:
    '''
    classdocs
    '''
    def __init__(self, element, tag="input"):
        '''
        Constructor
        '''
        self.__element = element
        self.__tag = tag
         
    def getValue(self):
        if self.__tag == "select":
            select = Select(self.__element)
            return select.all_selected_options() #返回是一个列表，所有被选中的项目放在列表里，option的列表
        else:
            return self.__element.text
    
    def setValue(self, value):
        if self.__tag == 'input' or self.__tag == 'textarea':
            self.__element.send_keys(value)
        elif self.__tag == 'select':
            select = Select(self.__element)
            select.select_by_visible_text(value)
    
    def click(self):
        self.__element.click()
    
    def clear(self, value=""):
        if self.__tag == "input" or self.__tag == "textarea":
            self.__element.clear()
        elif self.__tag == "select":
            select = Select(self.__element)
            if value != None:
                select.deselect_by_value(value)
            else:
                select.deselect_all()