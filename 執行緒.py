import time
import threading

def func1():
    print('Function 1 starting...')
    for i in range(1, 4):
        time.sleep(1)
        print(f'1-{i}')
    
        event.set()
    lock.acquire()
    print('Function 1 end')
    lock.release()

def func2():
    print('Function 2 starting...')
    for i in range(1, 4):
        
        event.wait()
        event.clear()
        
        time.sleep(1)
        print(f'2-{i}')
        
        event2.set()

    lock.acquire()
    print('Function 2 end')
    lock.release()

def func3():
    print('Function 3 starting...')
    for i in range(1, 4):
        event2.wait()
        event2.clear()
        
        time.sleep(1)
        print(f'3-{i}')
        
        event1.set()

    lock.acquire()
    print('Function 3 end')
    lock.release()

# 建立Lock物件
lock = threading.Lock()

event = threading.Event()
event1 = threading.Event()
event2 = threading.Event()

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

f1.join()
f2.join()
f3.join()

print(time.strftime('%H:%M:%S'))

event = threading.Event()