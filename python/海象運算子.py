# user = int(input('請輸入數字: '))

if (user := int(input('請輸入數字: '))) % 2 == 0:
    print(f'{user}為偶數')
else:
    print(f'{user}為奇數')