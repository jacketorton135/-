import time
import threading

def func1():
    print('Function 1 starting...')
    for i in range(30):
        time.sleep(0.1)
    print('Function 1 end')

def func2():
    print('Function 2 starting...')
    for i in range(30):
        time.sleep(0.1)
    print('Function 2 end')

def func3():
    print('Function 3 starting...')
    for i in range(30):
        time.sleep(0.1)
    print('Function 3 end')

# 建立執行緒
f1 = threading.Thread(target=func1)
f2 = threading.Thread(target=func2)
f3 = threading.Thread(target=func3)

print(time.strftime('%H:%M:%S'))
# func1()
# func2()
# func3()
f1.start() # 啟動func1執行緒
f2.start() # 啟動func2執行緒
f3.start() # 啟動func3執行緒
print(time.strftime('%H:%M:%S'))
        