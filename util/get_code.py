#coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time

class GetCode(object):
    def __init__(self,driver):
        self.driver = driver

    #获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        #print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        imgg = img.resize((790, 100),Image.ANTIALIAS)
        imgg.save(file_name)
        time.sleep(2)

    #解析图片获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","101098","f6b3ad5dad704d429c54583d1c19207b" )
        r.addBodyPara("img_base64", "utf-8")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)
        res = r.post()
        print(res.text)
        text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        return text