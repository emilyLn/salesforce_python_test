'''
Created on 2018年3月21日
'''
from .page import Page

class MenuPage(Page):
    '''
        菜单类
    '''

    def __init__(self, page_name="menu", file_suffix='yml'):
        super(MenuPage, self).__init__(page_name, file_suffix) #执行父类的构造方法，使用此种方式，可以一次执行所有父类的构造函数
        '''
                    要使用父类的__driver私有变量，由于私有变量不可继承，因此需要从get函数中取出来，在子类中定义一个同名的私有变量
                    如果要使用父类的函数修改父类的私有变量后，在子类中使用自己的私有变量，则需要通过父类定义的get方法取该变量的值
        '''
        self.__driver = self.driver
        self.__main_config = self.main_config
        
    def menu(self, element_name, *sub_elements):
        '''取一级菜单对应的元素'''
        self.loadWait(element_name)
        menu = self.element(element_name)
        '''定义一个list，作为取第二级及以下各级菜单元素的入参'''
        sub_element_list = []
        '''打开上级菜单，并取其下级菜单元素'''
        for sub_element in sub_elements:
            menu.click()
            '''
                            注意，元组操作的特点，创建一个只有一个元素的元组，这个唯一的元素后面一定要加一个逗号
                            元组内元素不可修改，但两个元组可以相加，组成一个新的元组
                            可变参数*param就是元组
            '''
            sub_element_list.append(sub_element)
            menu = self.element(element_name, *sub_element_list)
        return menu
        
    