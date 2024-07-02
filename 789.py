import pymysql

try:
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='oneokrock12345')

    cursor = conn.cursor()

    cursor.execute('show databases')

    for x in cursor:
        print(x)

except Exception as e:
    print('資料庫連線失敗: ', e)
