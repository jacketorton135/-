file = open('test.txt', 'w')  # with開啟的資源會自動做關閉

print('Hello Python', 'test', 'test', file=file)

file.close()