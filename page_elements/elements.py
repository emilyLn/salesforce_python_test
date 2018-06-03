'''
Created on 2018年3月23日
'''
from .element import Element
from utils.exceptions import CustmizeException

class Elements:
    '''
    classdocs
    '''
    def __init__(self, driver, by, search_str, tag):
        '''
        Constructor
        '''
        self.__by = by
        self.__search_str = search_str
        self.__tag = tag
        self.__driver = driver
        self.__elements = self.find_elements()
        
    def find_elements(self):
        if self.__search_str == "":
            raise CustmizeException("The search string is null, can't find element.")
        
        return self.__driver.find_elements(self.__by, self.__search_str)
    
    def select(self, index):
        if type(index) not in [int, str]:
            raise CustmizeException("只能通过行号或者行上的文本进行选择.")
        if type(index) == str:
            for element in self.__elements:
                sel = Element(element, self.__tag)
                if sel.getValue() == index:
                    return sel
                    break
        else:
            if index < 1:
                raise CustmizeException("行号不能小于1")
            elif index > self.__elements.length()-1:
                raise CustmizeException("行号超过总行数")
            return Element(self.__elements[index-1], self.__tag)
    
    def has(self, value):
        if type(value) != str:
            raise CustmizeException("只能判断文字是否存在.")
        for element in self.__elements:
            if element.text == value:
                return True
        return False
    
    def length(self):
        self.__elements.length()