import time
import warnings  
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


warnings.simplefilter('ignore',ResourceWarning)

browser = EdgeOptions()
browser.use_chromium = True
browser.binary_location = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" # 浏览器的位置
browser.add_argument(r"user-data-dir=C:/Users/PC-FT/AppData/Local/Microsoft/Edge/User Data") # 用户数据
# browser.add_argument('--headless') #不用打开图形界面
browser.add_argument('--disable-gpu')
browser.add_argument('--no-sandbox') #root权限
browser.add_experimental_option("detach", True)
browser.add_argument('--disable-dev-shm-usage')
browser.add_argument('--remote-debugging-port=9222')
browser.add_argument('--single-process')

driver = Edge(options=browser, executable_path=r"xxhelper/edge/edgedriver_win64/msedgedriver.exe") # 相应的浏览器的驱动位置

# "user-data-dir=D:/AAA/python/xxhelper/edge/edgedriver_win64/user"
# browser.maximize_window()   #设置浏览器大小：全屏
# driver.get('https://search.ll-dr.cn/booladmin/Home/Index')

time.sleep(1)

driver.get('https://search.ll-dr.cn/booladmin/Home/Login')

#定位输入框
login = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/button')
login.click()
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="OrderNo"]')))
input_box = driver.find_element_by_xpath('//*[@id="OrderNo"]')
try:
    input_box.send_keys('18127019376')
except Exception as e:
    print('fail')

#定位搜索按钮
button = driver.find_element_by_xpath('//*[@id="btnSelect"]')
try:
    button.click()
    print('成功搜索')
except Exception as e:
    print('fail搜索')

element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbls"]/table[2]')))

print(str(driver.find_element_by_xpath('//*[@id="tbls"]/table[2]/tbody/tr[2]/td[1]').text))
print(str(driver.find_element_by_xpath('//*[@id="tbls"]/table[2]/thead/tr/th[3]').text))
print(str(driver.find_element_by_xpath('//*[@id="tbls"]/table[2]/tbody/tr[5]/td[2]').text))
print(str(driver.find_element_by_xpath('//*[@id="tbls"]/table[2]/tbody/tr[1]/td[1]').text))
print(str(driver.find_element_by_xpath('//*[@id="tbls"]/table[2]/tbody/tr[2]/td[3]').text))
print(str(driver.find_element_by_xpath('//*[@id="tbls"]/table[2]/tbody/tr[8]/td[2]').text))
print(str(driver.find_element_by_xpath('//*[@id="tbls"]/table[2]/tbody/tr[3]/td[2]').text))

#clear()：清空输入框
try:
    input_box.clear()
    print('成功清空输入框')
except Exception as e:
    print('fail清空输入框')
#输出内容：成功清空输入框

time.sleep(1000)