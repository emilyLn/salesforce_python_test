# coding:UTF-8
from selenium import webdriver  
from .Common import Common
common = Common()
wb = common.Excel.workbook("C:\Python27\Data\Demo.xlsx")
sht = wb.worksheet("Login")

userId = sht.cell(1,2).getValue()
password = sht.cell(2,2).getValue()

sht = wb.worksheet("Data")

common.timeOut(30)
common.get("https://cs57.salesforce.com")
common.maximizeWindow()
common.LoginPage.userId().sendKeys(userId)
common.LoginPage.password().sendKeys(password)
common.LoginPage.loginButton().click()
common.Menu.MoreTabs_Tab().click()
common.Menu.MoreTabs_Tab().Item("日常工作计划").click()
common.DailyWorkPlanPage.newButton().click()

common.CreatePlanPage.startDate().sendKeys("2018-3-20")
common.CreatePlanPage.table().click()
common.CreatePlanPage.startTime().select("09:00")
common.CreatePlanPage.endTime().select("19:00")
common.CreatePlanPage.workContent().select("制定月度活动计划")
common.CreatePlanPage.saveButton().click()

planType = common.DailyWorkPlanDetailInformation.table("计划信息").field("计划类型").getText()
startDate = common.DailyWorkPlanDetailInformation.table("计划信息").field("开始日期").getText()
startTime = common.DailyWorkPlanDetailInformation.table("计划信息").field("开始时间").getText()
workContent = common.DailyWorkPlanDetailInformation.table("计划信息").field("工作内容").getText()
status = common.DailyWorkPlanDetailInformation.table("计划信息").field("状态").getText()
endDate = common.DailyWorkPlanDetailInformation.table("计划信息").field("结束时间").getText()

# assert planType=="计划外"
# assert startDate=="2018-3-19"
# assert startTime=="09:00"
# assert workContent=="制定月度活动计划"
# assert status=="未填写实际"
# assert endDate=="19:00"