import requests
import pandas as pd

# 指定 URL
url = "https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=csv"

# 發送 GET 請求下載 CSV 數據
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 將 CSV 數據讀取到 Pandas 數據框中
    data = pd.read_csv(pd.compat.StringIO(response.text))

    # 顯示數據框前五行
    print(data.head())
else:
    print("無法下載數據，請求失敗，狀態碼：", response.status_code)

