#coding=utf-8
from handle.register_hander import RegisterHandle
class RegisterBusiness(object):
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)

    #基础操作
    def user_base(self,email,name,password,file_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_button()

    #判断注册成功
    def register_success(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('code_text_error','验证码错误判断注册成功') == None:
            return True
        else:
            return False

    #email错误
    def login_email_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('email_error',"请输入有效的电子邮件地址") == None:
            print("邮箱格式检验不成功")
            return True
        else:
            print("邮箱格式验证成功")
            return False
    
    def register_function(self,email,username,password,file_name,assertCode,assertText):
        self.user_base(email,username,password,file_name)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            print("邮箱格式检验不成功")
            print("1111:",self.register_h.get_user_text(assertCode,assertText))
            return True
        else:
            print("邮箱格式验证成功")
            print("1111:",self.register_h.get_user_text(assertCode,assertText))
            return False    

    #name错误
    def login_name_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('name_error',"字符长度必须大于等于4，一个中文字算2个字符") == None:
            print("用户名检验不成功")
            return True
        else:
            return False
    
    #密码错误
    def login_password_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('password_error',"最少需要输入 5 个字符") == None:
            return True
        else:
            return False

    #验证码错误
    def login_code_error(self,email,name,password,file_name):
        self.user_base(email,name,password,file_name)
        if self.register_h.get_user_text('code_text_error',"验证码错误") == None:
            print("验证码验证不成功")
            return True
        else:
            return False