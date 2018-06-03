'''
Created on 2018年3月14日
'''

from utils.query_excel_data import Excel
from utils.commons import Commons
from test_cases.cases import Cases

USER_FILE_NAME = "test_data_login_users.xlsx"

class LoginAction:
    '''
        我们使用这个类做登录的公共类，提供了doLogin的登录的方法
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
#         self.__driver = driver
#         self.__config = Config(config=LOGIN_FILE) #将配置文件类的实例放到self的数据空间中
#     
    def doLogin(self):
        '''
        do login action
        '''
        '''取excel文件中的首页、用户名及密码的定义'''
        excel_data = Excel(USER_FILE_NAME)
        username = excel_data.cell(1, 'User')
        password = excel_data.cell(1, 'Password')
        '''
                    设置当前页面的对象并指定打开该页面对应的url。page函数的参数就是页面名称。如果是系统自动跳转到一个页面，则不需要调用open()
                    使用本框架，要求该名称与页面自己的配置文件的文件名相同（不带后缀的文件名部分），框架会自动找到该页面的配置文件，读取配置
        '''
        Cases.common.page("login").open()
        ''''首先选取一个元素，等待其加载后，再实际操作页面'''
        Cases.common.loadWait("btn_login")
        '''等待结束'''
        '''为元素赋值'''
        Cases.common.element("username").setValue(username)
        Cases.common.element("password").setValue(password)
        '''执行元素的click动作'''
        Cases.common.element("btn_login").click()
        
#         common.menu("m_more_tabs","m_daily_work_plan").click()
# #         
#         common.page("daily_work_plan")
#           
#         common.list("plan_names").select("A-000312").click()
# #         '''
#                 使用wait的方法，确保登录按钮可点之后才进行登录操作
#         '''
#         wait = WebDriverWait(self.__driver, 30)
#         wait.until(expected_conditions.element_to_be_clickable(login.getLocator("login_page_element","btn_login")))
#         '''
#                 按钮可点，等待结束
#         '''
#         login.assignUsername(username)
#         login.assignPassword(password)
#         login.doLogin()
#     
if __name__ == '__main__':  #独立测试login_action是否可用
    common = Commons()
    common.browser("chrome")
    login = LoginAction(common)
    login.doLogin()
    