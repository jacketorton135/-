import requests
from bs4 import BeautifulSoup

# 台灣銀行匯率網址
url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

response = requests.get(url)

with open('rate.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

with open('rate.html', 'r', encoding='utf-8') as file:
    data = file.read(135 * 1024 * 1000)
    
    soup = BeautifulSoup(data, 'html.parser')

    # print(soup.html.body.label)

    trs = soup.tbody.find_all('tr')
    
    for i in trs:
        print(i.td.div.find_all('div')[1].text.strip())
        
        flag = i.find(title='幣別國旗')
    
        q = {'data-table':'本行現金買入'}
        flag = i.find(attrs=q)
        
        print(f'  - 現金買入: {flag.text}')   
        
        q = {'data-table':'本行即期買入'}
        flag = i.find(attrs=q)
        
        print(f'  - 即期買入: {flag.text.strip()}')  
        
        
        q = {'data-table': '本行即期賣出'}
        flag = i.find(attrs=q)
        
        print(f'  - 本行即期賣出: {flag.text.strip()}')  
        
   