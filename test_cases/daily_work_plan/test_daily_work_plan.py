'''
Created on 2018年3月14日
'''
import unittest
import time
from test_cases.login_action import LoginAction
from test_cases.cases import Cases
from utils.query_excel_data import Excel
from utils.datetimes import compareDateTime
from selenium.common.exceptions import NoAlertPresentException

class DailyWorkPlanCases(unittest.TestCase):
    # TestCase基类方法,所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        Cases()
        Cases.common.browser("chrome")
        LoginAction().doLogin()
        print("这里是所有测试用例前的准备工作")

    # TestCase基类方法,所有case执行之后自动执行
    @classmethod
    def tearDownClass(cls):
        Cases.common.close()
        print("这里是所有测试用例后的清理工作")

    # TestCase基类方法,每次执行case前自动执行
    def setUp(self):
        print("这里是一个测试用例前的准备工作")

    # TestCase基类方法,每次执行case后自动执行
    def tearDown(self):
        print("这里是一个测试用例后的清理工作")

    @unittest.skip("我想临时跳过这个测试用例.")
    def test001_NewPlan(self):
        Cases.common.menu("m_more_tabs","m_daily_work_plan").click()
        Cases.common.page("daily_work_plan")
        Cases.common.element("btn_new").click()
        '''
                    进入新建页面，开始新建日常工作计划的操作
        '''
        Cases.common.page("daily_work_plan_new")
        excel_data = Excel("test_data_dailyworkplannew.xlsx")
        #第一步，赋值
        Cases.common.element("plan_date").setValue(excel_data.cell(1, "plan_date"))
        Cases.common.element("start_time").setValue(excel_data.cell(1, "start_time"))
        Cases.common.element("end_time").setValue(excel_data.cell(1, "end_time"))
        Cases.common.element("plan_content").setValue(excel_data.cell(1, "plan_content"))
        #第二步，保存
        Cases.common.element("btn_save").click()
         
        '''
                 验证结果
        '''
        Cases.common.page("daily_work_plan_detail")
        Cases.common.loadWait("page_description")
        
        self.assertEqual(excel_data.cell(1, "plan_content"), Cases.common.element("plan_info","plan_content").getValue(), msg='新增后保存的信息不正确')
    
    @unittest.skip("我想临时跳过这个测试用例.")
    def test002_DailyWorkPlanDetail(self):
        Cases.common.menu("m_more_tabs","m_daily_work_plan").click()
        Cases.common.page("daily_work_plan")
        excel_data = Excel("test_data_dailyworkplan.xlsx")
        #从文件中取要选择的计划名
        Cases.common.list("plan_names").select(excel_data.cell(1, "plan_name")).click()
        
        '''验证结果'''
        Cases.common.page("daily_work_plan_detail")
        Cases.common.loadWait("page_description")
        self.assertEqual(excel_data.cell(1, "plan_name"), Cases.common.element("page_description").getValue(), msg='保存后跳转页面错误')
     
    #@unittest.skip("我想临时跳过这个测试用例.")
    def test003_DailyWorkPlanModify(self):
        Cases.common.menu("m_more_tabs","m_daily_work_plan").click()
        Cases.common.page("daily_work_plan")
        excel_data = Excel("test_data_dailyworkplan.xlsx")
        #从文件中取要选择的计划名
        Cases.common.list("plan_names").select(excel_data.cell(1, "plan_name")).click()
        
        #取得当前计划的状态，用来判断修改计划的操作结果
        Cases.common.page("daily_work_plan_detail")
        plan_status = Cases.common.element("plan_info","plan_status").getValue()
        plan_date = Cases.common.element("plan_info","plan_date").getValue()
        
        Cases.common.element("btn_modify").click()
        if plan_status != '未填写实际': #不等于未填写实际，则不可以修改计划
            dialog = Cases.common.switchtoAlert()
            self.assertEqual("已取消和已填写实际的计划，无法修改计划。",dialog.getMsg(),"提示信息错误")
            dialog.accept() #no_modify_inf.dismiss()
        elif Cases.common.compareDate(plan_date, Cases.common.currentDate()) <= 0: #计划日期小于当前日期的case，应该弹出提示信息，不可修改
            dialog = Cases.common.switchtoAlert()
            self.assertEqual("时限已过，无法修改计划。",dialog.getMsg(),"提示信息错误")
            dialog.accept() #no_modify_inf.dismiss()
        else:
            dialog = Cases.common.switchtoAlert()
            self.assertEqual("是否确认修改计划?",dialog.getMsg(),"提示信息错误")
            dialog.accept() #no_modify_inf.dismiss()
            
            Cases.common.page("daily_work_plan_modify")
            Cases.common.loadWait("start_time")
            excel_data = Excel("test_data_dailyworkplandetail.xlsx")
            Cases.common.element("start_time").setValue(excel_data.cell(1,"start_time"))
            Cases.common.element("end_time").setValue(excel_data.cell(1,"end_time"))
            Cases.common.element("plan_content").setValue(excel_data.cell(1,"plan_content"))
             
            #第二步，保存
            Cases.common.element("btn_save").click()
            #判断结果
            Cases.common.page("daily_work_plan_detail")
            Cases.common.loadWait("plan_info")
            self.assertEqual(excel_data.cell(1,"plan_content"),Cases.common.element("plan_info","plan_content").getValue(),"数据修改失败")
     
#     @unittest.skip("我想临时跳过这个测试用例.")
    def test004_DailyWorkPlanRecord(self): #填写记录
        Cases.common.menu("m_more_tabs","m_daily_work_plan").click()
        Cases.common.page("daily_work_plan")
        excel_data = Excel("test_data_dailyworkplan.xlsx")
        #从文件中取要选择的计划名
        Cases.common.list("plan_names").select(excel_data.cell(1, "plan_name")).click()
        
        #取得当前计划的状态，用来判断修改计划的操作结果
        Cases.common.page("daily_work_plan_detail")
#         #取得当前计划的状态，用来判断修改计划的操作结果
#         plan_status = daily_work_plan_detail.findElement("detail_page_element","plan_info","plan_status").text
#         plan_date = daily_work_plan_detail.findElement("detail_page_element","plan_info","plan_date").text#
#         current_date = utils.datetimes.getCurrentDate()
#         daily_work_plan_detail.recordActual()
#         
#         if utils.datetimes.compareDateTime(plan_date, current_date, "%Y-%m-%d") > 0: #计划日期大于当前日期
#             time.sleep(2)
#             no_modify_info = daily_work_plan_detail.catchPopupDialog()
#             print(no_modify_info.text)
#             self.assertEqual("开始日期未到，当前工作记录不可填写实际。",no_modify_info.text,"提示信息错误")
#             no_modify_info.accept() #no_modify_inf.dismiss()
#         elif plan_status == '已填写实际' or plan_status == '未填写实际':
#             daily_work_plan_record = DailyWorkPlanRecord(self.driver)
#             daily_work_plan_record.assignActualStartTime("09:00")
#             daily_work_plan_record.assignActualEndTime("18:00")
#             daily_work_plan_record.assignActualContent("活动前消费者邀约")
#             daily_work_plan_record.assignNoActionReason("已完成")
#             daily_work_plan_record.assignActualStatus("进展顺利")
#             
#             daily_work_plan_record.save()
#             wait = WebDriverWait(self.driver, 60)
#             wait.until(expected_conditions.visibility_of_element_located(daily_work_plan_detail.getLocator("detail_page_element","plan_info","plan_content")))
#             self.assertEqual("活动前消费者邀约",daily_work_plan_detail.findElement("detail_page_element","actual_info","actual_content").text,"")
#     
#     def test005_DailyWorkPlanCancel(self):  
#         daily_work_plan_detail = DailyWorkPlanDetail(self.driver)
#         plan_name = 'A-000186'
#         daily_work_plan_detail.enterDailyWorkPlanDetail(plan_name) #进入日常工作计划主界面
#         
#         #取得当前计划的状态，用来判断取消计划的操作结果
#         plan_status = daily_work_plan_detail.findElement("detail_page_element","plan_info","plan_status").text
#         
#         daily_work_plan_detail.cancelPlan()
#         if plan_status == '已填写实际' or plan_status == '已取消':
#             time.sleep(2)
#             no_modify_info = daily_work_plan_detail.catchPopupDialog()
#             print(no_modify_info.text)
#             self.assertEqual("已取消或已填写实际的的计划不可取消。",no_modify_info.text,"提示信息错误")
#             no_modify_info.accept() #no_modify_inf.dismiss()
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()