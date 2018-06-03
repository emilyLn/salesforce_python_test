'''
Created on 2018年3月20日
'''
from .browser import Browser
from pages.page import Page
from pages.menu_page import MenuPage
from utils.exceptions import CustmizeException
from utils.datetime import getCurrentDate
from utils.datetime import compareDateTime

class Commons:
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__page = None #初始化page为空
        self.__menu = None
        
    def browser(self, browser_type="firefox"):
        Browser(browser_type)
        
    def page(self, page_name, menu_name="menu"):
        self.__page = Page(page_name)
        if self.__menu == None:
            self.__menu = MenuPage(menu_name)
        return self.__page
    
    def element(self, element_name, *subelement):
        if self.__page == None:
            raise CustmizeException("当前没有打开的页面，不能操作菜单")
        
        return self.__page.element(element_name, *subelement)
    
    def list(self, element_name, *sub_element):
        if self.__page == None:
            raise CustmizeException("当前没有打开的页面，不能操作菜单")
        
        return self.__page.list(element_name, *sub_element)
    
    def menu(self, menu_name, *sub_menu):
        if self.__page == None:
            raise CustmizeException("当前没有打开的页面，不能操作菜单")
        
        return self.__menu.menu(menu_name, *sub_menu)
    
    def loadWait(self, element):
        if self.__page == None:
            raise CustmizeException("当前没有打开的页面，不能操作菜单")
        
        self.__page.loadWait(element)
    
    def close(self):
        self.__page.pageClose()
        
    def switchtoAlert(self):
        return self.__page.switchtoAlert()
    
    def currentDate(self):
        print("in currentDate func")
        return getCurrentDate()
    
    def compareDate(self, firstDate, secondDate):
        return compareDateTime(firstDate, secondDate, "%Y-%m-%d")