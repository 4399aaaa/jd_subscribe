import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
token=os.environ['PLUS_KEY']
plant1=os.environ['PLANT1']
fruit1=os.environ['FRUIT1']
pet1=os.environ['PET1']
dream_factory1=os.environ['DREAM_FACTORY1']
jd_factory1=os.environ['JD_FACTORY1']
def jd_subscribe(plant_code,fruit_code,pet_code,dream_factory_code,jd_factory_code):
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
        dream_factory_url = "http://api.turinglabs.net/api/v1/jd/jxfactory/create/"+str(dream_factory_code)+"/"
        jd_factory_url = "http://api.turinglabs.net/api/v1/jd/ddfactory/create/"+str(jd_factory_code)+"/"
        driver.get(plant_code_url)
        driver.implicitly_wait(100)
        driver.get(fruit_code_url)
        driver.implicitly_wait(100)
        driver.get(pet_code_url)
        driver.implicitly_wait(100)
        driver.get(dream_factory_url)
        driver.implicitly_wait(100)
        driver.get(jd_factory_url)
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
if __name__ == "__main__":
   jd_subscribe(plant1,fruit1,pet1,dream_factory1,jd_factory1)
