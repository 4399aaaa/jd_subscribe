import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
token=os.environ['PLUS_KEY']
def jd_subscribe(plant_code,fruit_code,pet_code,dream_factory_code):
    try:
        # 模拟浏览器打开网站
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
        plant_code_url = "http://api.turinglabs.net/api/v1/jd/bean/create/"+str(plant_code)+"/"
        fruit_code_url = "http://api.turinglabs.net/api/v1/jd/farm/create/"+str(fruit_code)+"/"
        pet_code_url = "http://api.turinglabs.net/api/v1/jd/pet/create/"+str(pet_code)+"/"
        dream_factory_url= "http://api.turinglabs.net/api/v1/jd/jxfactory/create/"+str(dream_factory_code)+"/"
        driver.get(plant_code_url)
        driver.implicitly_wait(100)
        driver.get(fruit_code_url)
        driver.implicitly_wait(100)
        driver.get(pet_code_url)
        driver.get(dream_factory_url)
        driver.implicitly_wait(100)
    except:
        driver.quit()
        print("上车失败!")
        title= '京东互助上车执行情况' #改成你要的标题内容
        content ='上车失败' #改成你要的正文内容
        url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token+'&title='+title+'&content='+content
        requests.get(url)
    else:
        driver.quit()
        print("上车成功")
        title= '京东互助上车执行情况' #改成你要的标题内容
        content ='上车成功' #改成你要的正文内容
        url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token+'&title='+title+'&content='+content
        requests.get(url)
 #种豆得豆部分
plant_code = os.environ['PLANT']  # 此时是字符串，记得一定要加引号啊。
plant_code_num = int(plant_code.count('&'))+1
print("你输入了%d个种豆得豆互助码" % plant_code_num)
list1 = plant_code.split("&")

#水果部分
fruit_code = os.environ['FRUIT']
fruit_code_num = int(fruit_code.count('&'))+1
print("你提供了%d个水果互助码" % fruit_code_num)
list2 = fruit_code.split("&")

#东东萌宠部分
pet_code = os.environ['PET']
pet_code_num = int(pet_code.count('&'))+1
print("你提供了%d个东东萌宠互助码" % pet_code_num)
list3 = pet_code.split("&")

#京喜工厂部分
dream_factory_code = os.environ['DREAM_FACTORY']
dream_factory_code_num = int(dream_factory_code.count('&'))+1
print("你提供了%d个京喜工厂互助码" % dream_factory_code_num)
list4 = dream_factory_code.split("&")
if __name__ == "__main__":
    for i in range(fruit_code.count('&')+1):
        jd_subscribe(list1[i],list2[i],list3[i],list4[i])

