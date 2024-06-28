import random

answer = random.randint(1, 10)
print(f'答案:{answer}')
user = int(input('請隨機猜1-10數字: '))

if answer == user:

  print('猜對了')   
else:
  print('猜錯了')