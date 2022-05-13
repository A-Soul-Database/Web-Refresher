from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import multiprocessing
import os
import random
import time
Start_Time = time.time()
Config = json.loads(open("./Config.json","r",encoding="utf-8").read())
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument(f"user-agent={Config['User-Agent']}")
chrome_options.add_argument('--incognito')

def Open_Tasks(url:str,nums:int):
    driver = webdriver.Chrome(chrome_options = chrome_options)
    times = 0
    while True:
        assert driver.get(url) != None , os.system('echo    "Error in opening {url}"')
        time.sleep(random.randint(Config['Random_Durations']))
        driver.refresh()
        os.system(f'echo "{time.time()-Start_Time} : Process {nums} for {url} has Refershed {times} times"')
        times+=1
        time.sleep(1)

if __name__ == '__main__':
    for i in Config["Urls"]:
        for n in range(Config["Process_Nums"]):
            multiprocessing.Process(target=Open_Tasks,args=(i,n,)).start()