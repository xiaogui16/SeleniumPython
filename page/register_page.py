#coding=utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.find_e = FindElement(driver)
    
    #获取邮箱元素
    def get_email_element(self):
        return self.find_e.get_element('user_email')
    
    #获取用户名元素
    def get_username_element(self):
        return self.find_e.get_element('user_name')
    
    #获取密码元素
    def get_password_element(self):
        return self.find_e.get_element('password')

    #获取验证码元素
    def get_code_element(self):
        return self.find_e.get_element('code_text')

    #点击事件
    def get_button_element(self):
        return self.find_e.get_element('register_button')

    #获取邮箱输入错误提示的元素
    def get_email_error_element(self):
        return self.find_e.get_element('user_email_error')
    
    #获取用户名输入错误提示的元素
    def get_name_error_element(self):
        return self.find_e.get_element('user_name_error')
    
    #获取密码输入错误提示的元素
    def get_password_error_element(self):
        return self.find_e.get_element('password_error')
    
    #获取验证码输入错误提示的元素
    def get_code_error_element(self):
        return self.find_e.get_element('code_text_error')