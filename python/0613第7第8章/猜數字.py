import random

answer = random.randint(1, 10)
print(f'測試用: {answer}')

count = 0 # 紀錄總共猜了幾次

while True:
    user = int(input('請猜一個數字: '))
    count += 1  # 加一次

    if user == answer:
        print(f'猜對了，總共猜了{count}次')
        break
    else:
        print(f'猜錯了，已經猜了{count}次')