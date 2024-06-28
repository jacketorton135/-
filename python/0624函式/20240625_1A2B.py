import random

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

answer = random.sample(a, 4)

answer = answer[0] + answer[1] + answer[2] + answer[3]
# answer = ''.join(answer)

print(f'答案: {answer}')

count = 0 # 存次數

while True:
    user = input('請猜四位數數字(數字不可重複): ')
    count += 1

    # 判斷輸入的文字是不是數字
    try:
        int(user)
    except ValueError:
        print('只能輸入數字，請重新輸入')
        continue

    # 輸入的數字是否為四位數
    if len(user) != 4:
        print('只能輸入四位數')
        continue

    # 輸入的數字是否重複
    if len(set(user)) != 4:
        print('輸入的數字不可重複')
        continue

    if answer == user:
        print(f'猜對了，總共猜了{count}次')
        break

    # 判斷幾個A
    how_many_A = 0

    if answer[0] == user[0]:
        how_many_A += 1

    if answer[1] == user[1]:
        how_many_A += 1

    if answer[2] == user[2]:
        how_many_A += 1

    if answer[3] == user[3]:
        how_many_A += 1

    # 判斷幾個B
    how_many_B = 0
    if user[0] in answer and user[0] != answer[0]:
        how_many_B += 1
    if user[1] in answer and user[1] != answer[1]:
        how_many_B += 1
    if user[2] in answer and user[2] != answer[2]:
        how_many_B += 1
    if user[3] in answer and user[3] != answer[3]:
        how_many_B += 1

    print(f'{how_many_A}A{how_many_B}B')
