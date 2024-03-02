from selenium import webdriver
# 在这里导入浏览器设置相关的类
from selenium.webdriver.edge.options import Options
from msedge.selenium_tools import Edge, EdgeOptions
 
# 无可视化界面设置 #
 
edge_options = EdgeOptions()
# 使用无头模式
edge_options.add_argument('--headless')
# 禁用GPU，防止无头模式出现莫名的BUG
edge_options.add_argument('--disable-gpu')
edge_options.use_chromium = True
edge_options.binary_location = r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" # 浏览器的位置
edge_options.add_argument(r"user-data-dir=C:/Users/PC-FT/AppData/Local/Microsoft/Edge/User Data") # 用户数据
edge_options.add_argument('--headless') #不用打开图形界面
edge_options.add_argument('--disable-gpu')
edge_options.add_argument('--no-sandbox') #root权限
edge_options.add_experimental_option("detach", True)
edge_options.add_argument('--disable-dev-shm-usage')
edge_options.add_argument('--remote-debugging-port=9222')
edge_options.add_argument('--single-process')
 
# 将参数传给浏览器
# browser = webdriver.Edge(options=edge_options, executable_path=r"xxhelper/edge/edgedriver_win64/msedgedriver.exe")
browser = Edge(options=edge_options, executable_path=r"xxhelper/edge/edgedriver_win64/msedgedriver.exe") # 相应的浏览器的驱动位置
 
# 启动浏览器
url = "https://baidu.com"
browser.get(url)
print(browser.title)
 
# 关闭浏览器
browser.quit()