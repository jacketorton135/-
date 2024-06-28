import random

answer = random.randint(1, 100)
print(f'答案: {answer}')

min = 1
max = 100

count = 0

while True:
    user = input(f'請猜 {min} ~ {max} 之間的數字(目前猜了{count}次): ')
    count += 1

    # error handling
    if user.isdigit():
        user = int(user)
    else:
        print('輸入錯誤，只能輸入數字，請重新輸入')
        continue

    if user < min or user > max:
        print(f'輸入錯誤，超出{min}~{max}範圍，請重新輸入')
        continue

    if user < answer:
        min = user + 1
    elif user > answer:
        max = user - 1
    else:
        print(f'猜對了，總共猜了{count}次')
        break