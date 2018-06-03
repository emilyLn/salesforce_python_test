'''
Created on 2018年3月20日
'''
import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH, REPORT_PATH

# 可根据需要自行扩展
CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

class Browser:
    '''
    classdocs
    '''
    driver = None #类变量，使用Browser.driver在所有实例间共享
    
    def __init__(self, browser_type='firefox'):
        self.__type = browser_type.lower()
        if self.__type in TYPES:
            self.__browser = TYPES[self.__type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        '''初始化Browser类，即为创建一个新的webdriver'''
        Browser.driver = self.__browser(executable_path=EXECUTABLE_PATH[self.__type])
    
    def open(self, url, maximize_window=True):
        Browser.driver.open(url)
        if maximize_window:
            Browser.driver.maximize_window()
#     def get(self, url, maximize_window=True, implicitly_wait=30):
#         self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
#         self.driver.get(url)
#         if maximize_window:
#             self.driver.maximize_window()
#         self.driver.implicitly_wait(implicitly_wait)
#         return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = Browser.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        Browser.driver.close()

    def quit(self):
        Browser.driver.quit()