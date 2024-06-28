import requests
import csv
import time
from bs4 import BeautifulSoup

# PTT Python 版块网址
url = 'https://www.ptt.cc/bbs/Python/index.html'

# 发送请求获取页面内容
response = requests.get(url)

# 解析 HTML 内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到包含文章标题的元素
titles = soup.find_all('div', class_='title')

# 准备存储文章标题的列表
titles_list = []

# 输出所有文章标题
for title in titles:
    a_tag = title.find('a')
    if a_tag:
        title_text = a_tag.text.strip()
        print(f' - 標題: {title_text}')
        titles_list.append([title_text])

# 创建文件名（当前时间作为文件名）
filename = f'{time.strftime("%Y%m%d_%H%M%S")}.csv'

# 写入 CSV 文件
with open(filename, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(titles_list)

print(f'CSV 文件 {filename} 写入完成。')
