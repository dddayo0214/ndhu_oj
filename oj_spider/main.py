#coding = utf-8
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('http://134.208.3.66/problem?page=2&limit=10')

time.sleep(2)

problems = driver.find_elements(By.CLASS_NAME, 'ivu-table-row')

print(len(problems))
# if len(problems):
#     driver.quit()