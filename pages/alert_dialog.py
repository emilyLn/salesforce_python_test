'''
Created on 2018年3月23日

'''

class AlertDialog:
    '''
    deal with "alert、confirm、prompt" dialog
    '''

    def __init__(self, dialog_handle):
        '''
        Constructor
        '''
        self.__dialog_handle = dialog_handle
    
    def accept(self):
        self.__dialog_handle.accept()
    
    def dismiss(self):
        self.__dialog_handle.dismiss()
    
    def getMsg(self):
        return self.__dialog_handle.text
    
    def setMsg(self, value):
        self.__dialog_handle.send_keys(value)
        