from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

# 初始化Chrome瀏覽器驅動程式
driver =  webdriver.Chrome()

# 載入網頁時要等待的時間(秒)
driver.implicitly_wait(10)

# 用Chrome瀏覽器打開網頁
driver.get('https://www.youbike.com.tw/region/main/login/')

# 印出網頁標題
print(driver.title)


# 解析資料
confirm_btn= driver.find_element(By.LINK_TEXT, '確定')
confirm_btn.click()
time.sleep(2)

phone_input = driver.find_element(By.NAME, 'phone')
phone_input.send_keys('0984306550')
time.sleep(2)

password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('Oneokrock12345')
time.sleep(2)

Login_btn = driver.find_element(By.LINK_TEXT, '登入')
login_btn_click()
time.sleep(2)