'''
Created on 2018年3月20日
'''
import os
from utils.file_reader import ExcelReader
from utils.config import TEST_MODULE_PATH
from utils.exceptions import CustmizeException

class Excel(ExcelReader):
    '''
        取excel测试数据的基类(支持xls和xlsx)
    '''
    def __init__(self, excelfile, path = TEST_MODULE_PATH, sheet=0, title_line=True):
        '''
        Constructor
        '''
        excel_path = os.path.join(path, excelfile)
        super(Excel, self).__init__(excel_path, sheet, title_line)
    
    def cell(self, line, column):
        if type(line) != int:
            raise CustmizeException("please input a line number")
        if line < 1:
            raise CustmizeException("line number must greater than 1")
        return self.data[line-1][column]