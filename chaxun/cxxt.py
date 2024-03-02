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

def jqbcx():
    browser.add_argument('--disable-gpu')
    time.sleep(1)

    driver.get('https://search.ll-dr.cn/booladmin/Home/Login')

    #定位输入框
    login = driver.find_element_by_xpath('/html/body/div/div/div/div[4]/button')
    login.click()

        
def startcx():
    browser.add_argument('--disable-gpu')
    element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="OrderNo"]')))
    input_box = driver.find_element_by_xpath('//*[@id="OrderNo"]')
    try:
        input_box.send_keys('18127019376')
    except Exception as e:
        print('fail')

time.sleep(1000)