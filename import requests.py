from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 设置 ChromeDriver 的路径
chrome_driver_path = "path/to/chromedriver"  # 替换为实际路径

# 设置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 以无头模式运行

# 创建 ChromeDriver 服务
service = Service(chrome_driver_path)

# 创建 WebDriver 实例
driver = webdriver.Chrome(service=service, options=chrome_options)

# 访问目标 URL
url = 'https://tw.stock.yahoo.com/quote/2330.TW'
driver.get(url)

# 等待页面加载并找到元素
driver.implicitly_wait(10)  # 等待最多 10 秒

# 获取股票名称和股价
stock_name = driver.find_element(By.CSS_SELECTOR, 'h1[class*="D(ib)"]').text
stock_price = driver.find_element(By.CSS_SELECTOR, 'fin-streamer[data-field="regularMarketPrice"]').text

# 输出股票名称和股价
print(f"股票名稱: {stock_name}")
print(f"股價: {stock_price}")

# 关闭 WebDriver
driver.quit()
