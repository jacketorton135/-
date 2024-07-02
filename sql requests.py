import requests
import pandas as pd
from sqlalchemy import create_engine

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

    # 建立 MySQL 連接引擎
    engine = create_engine("mysql+pymysql://root:oneokrock12345@localhost/jack")

    # 將數據插入到 MySQL 資料庫的 member 表中
    data.to_sql('member', con=engine, if_exists='append', index=False)

    print("數據已成功插入到 MySQL 資料庫中。")
else:
    print("無法下載數據，請求失敗，狀態碼：", response.status_code)
