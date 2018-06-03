'''
Created on 2018年3月14日
'''
from .base_page import BasePage
from utils.config import LOGIN_FILE

class LoginPage(BasePage):
    '''
        提供登录界面的控件的读取方法以及登录操作对于控件的使用方法
    '''
    
    def __init__(self, driver,config_file_name=LOGIN_FILE):
        super(LoginPage, self).__init__(driver, config_file_name) #执行父类的构造方法，使用此种方式，可以一次执行所有父类的构造函数
        self.__name = "LoginPage"
    
    @property
    def name(self):
        return self.__name
        
    def assignUsername(self, username):
        self.assignElement(username, "login_page_element", "username")
    
    def assignPassword(self, password):
        self.assignElement(password, "login_page_element", "password")
        
    def doLogin(self): 
        '''
                    点击“登录 sendbox”按钮
        '''
        self.findElement("login_page_element", "btn_login").click()
        