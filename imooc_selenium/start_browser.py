#coding:utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))
locator = (By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))

email_element = driver.find_element_by_id("register_email")
driver.find_element_by_id("register_email").send_keys("zhufenglove2007@163.com")
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
user_name = user_name_element_node.find_element_by_class_name("form-control")
user_name.send_keys("dfdfdf")
driver.find_element_by_name("password").send_keys("111111")
#driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("343434")

driver.save_screenshot("E:/learner/Imooc/imooc2.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open("E:/learner/Imooc/imooc2.png")
img = im.crop((left,top,right,height))
imgg = img.resize((790, 100),Image.ANTIALIAS)
imgg.save("E:/learner/Imooc/imooc3.png")


r = ShowapiRequest("http://route.showapi.com/184-4","101098","f6b3ad5dad704d429c54583d1c19207b" )
r.addBodyPara("img_base64", "utf-8")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"E:/learner/Imooc/imooc3.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
driver.find_element_by_id("captcha_code").send_keys(text)
#随机获取用户名或者邮箱
#for i in range(5):
    #user_email = ''.join(random.sample('1234567890abcdefg',5))+"@163.com"
    #print(user_email)
#print(email_element.get_attribute("placeholder"))
#email_element.send_keys("zhufenglove2007@163.com")
#print(email_element.get_attribute("value"))
driver.close()