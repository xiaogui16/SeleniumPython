#coding=utf-8
import sys
sys.path.append("E:/SELENIUMPYTHON")
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import unittest
import warnings
import HTMLTestRunner
import os
import time

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.logger.info("this is chrome")
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

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34','user1111','111111',self.file_name)
        self.assertFalse(email_error)
        #通过assert判断是否为error

    def test_login_username_error(self):
        username_error = self.login.login_name_error('111@163.com','s1s','33434',self.file_name)
        self.assertFalse(username_error)

    def test_login_password_error(self):
        password_error = self.login.login_password_error('12112@163.com','ss','3343',self.file_name)
        self.assertFalse(password_error)

    def test_login_code_error(self):
        code_error = self.login.login_code_error('12112@163.com','ss','33434',self.file_name)
        self.assertFalse(code_error)

    def test_login_success(self):
        success = self.login.register_success('test16@163.com','test16','33434',self.file_name)
        #self.assertFalse(success)
        self.assertEqual(True,success)

'''
def main():
    first = FirstCase()
    first.test_login_email_error()
    #first.test_login_username_error()
    #first.test_login_password_error()
    #first.test_login_code_error()
    #first.test_login_success()
'''

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"/report/"+"first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    #suite.addTest(FirstCase('test_login_password_error'))
    #suite.addTest(FirstCase('test_login_code_error'))
    #suite.addTest(FirstCase('test_login_success'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report",description=u"这是我们第一次测试报告",verbosity=2)
    runner.run(suite)