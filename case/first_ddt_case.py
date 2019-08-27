#coding=utf-8
import sys
sys.path.append("E:/SELENIUMPYTHON")
from business.register_business import RegisterBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import unittest
import HTMLTestRunner
import os
import time
import ddt
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)
        self.file_name = "E:/SELENIUMPYTHON/Image/test001.png"

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
        print("执行完一条case")

    '''
    @ddt.data(
            ['test001','username01','password','code','user_email_error','请输入有效的电子邮件地址'],
            ['@qq.com','username01','password','code','user_email_error','请输入有效的电子邮件地址'],
            ['test001@qq.com','username01','password','code','user_email_error','请输入有效的电子邮件地址']
    )

    @ddt.unpack  
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        email,username,password,code,assertCode,assertText = data
        email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(email_error,"测试失败")

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report1",description=u"这是我们第一次测试报告1",verbosity=2)
    runner.run(suite)