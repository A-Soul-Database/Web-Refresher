from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib import parse
import json
import multiprocessing
import os
import random
import time
Start_Time = time.time()
Config = json.loads(open("./Config.json","r",encoding="utf-8").read())
chrome_options = Options()
#chrome_options.binary_location = "./GoogleChromePortable/App/Chrome-bin/chrome.exe"
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument(f"user-agent={Config['User-Agent']}")
chrome_options.add_argument('--incognito')


def Open_Tasks(tag:str,nums:int):
    driver = webdriver.Chrome(chrome_options=chrome_options)
                              #,executable_path="./GoogleChromePortable/chromedriver.exe")
    times = 0
    while True:
        times+=1
        driver.get(f"https://s.weibo.com/weibo?q={parse.quote(tag)}")
        time.sleep(3)
        os.system(f'echo "{time.time()-Start_Time} : 进程ID: {nums} 打开了, 标题: {driver.title}"')
        time.sleep(random.randint(Config['Random_Durations'][0],Config['Random_Durations'][1]))
        driver.refresh()
        os.system(f'echo "{time.time()-Start_Time} : 进程ID: {nums} 刷新了 {times} 次"')
        time.sleep(1)

if __name__ == '__main__':
    for i in Config["Tags"]:
        for n in range(Config["Process_Nums"]):
            multiprocessing.Process(target=Open_Tasks,args=(i,n,)).start()
