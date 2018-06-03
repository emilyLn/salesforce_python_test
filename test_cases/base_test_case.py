'''
Created on 2018年3月23日

@author: Emily
'''
import unittest
from utils.commons import Commons

class BaseTestCase(unittest.TestCase):
    common = None
    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        cls.common = Commons()
        cls.common.browser("chrome")
        
        print("这里是所有测试用例前的准备工作")

    # TestCase基类方法,所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        cls.common.close()
        print("这里是所有测试用例后的清理工作")

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()