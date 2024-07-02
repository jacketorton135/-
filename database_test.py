import pymysql

try:
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='xxxxxx')

    cursor = conn.cursor()

    cursor.execute('show databases')

    for i in cursor:
        print(i)

except Exception as e:
    print('資料庫連線失敗: ', e)
