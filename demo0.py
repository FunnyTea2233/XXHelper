from selenium import webdriver
import time  
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By

browser = EdgeOptions()
browser.use_chromium = True
browser.binary_location = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" # 浏览器的位置
driver = Edge(options=browser, executable_path=r"D:/AAA/python/xxhelper/edge/edgedriver_win64/msedgedriver.exe") # 相应的浏览器的驱动位置
# browser.maximize_window()   #设置浏览器大小：全屏
driver.get('https://www.baidu.com')
 
time.sleep(3)
#定位输入框

input_box = driver.find_element_by_id('kw')
try:
    #输入内容：selenium
    input_box.send_keys('selenium')
    print('搜索关键词：selenium')
except Exception as e:
    print('fail')
#输出内容：搜索关键词：selenium

#定位搜索按钮
button = driver.find_element_by_id('su')
try:
    #点击搜索按钮
    button.click()
    print('成功搜索')
except Exception as e:
    print('fail搜索')
#输出内容：成功搜索

#clear()：清空输入框
try:
    input_box.clear()
    print('成功清空输入框')
except Exception as e:
    print('fail清空输入框')
#输出内容：成功清空输入框