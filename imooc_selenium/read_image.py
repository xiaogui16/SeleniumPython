#coding:utf-8
import pytesseract
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
#image = Image.open("E:/imooc1.png")
#text = pytesseract.image_to_string(image)
#print(text)
r = ShowapiRequest("http://route.showapi.com/184-4","101098","f6b3ad5dad704d429c54583d1c19207b" )
r.addBodyPara("img_base64", "utf-8")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"E:/imooc1.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息