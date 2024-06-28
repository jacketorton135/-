year = int(input('請輸入民國年: '))
print(f'民國{year}年 = 西元{year+1911}年')

smile = year % 12

if smile == 1:
    print(f'{year}為鼠年')
elif smile == 2:
    print(f'{year}為牛年')
elif smile == 3:
    print(f'{year}為虎年')
elif smile == 4:
    print(f'{year}為兔年')
elif smile == 5:
    print(f'{year}為龍年')
elif smile == 6:
    print(f'{year}為蛇年')
elif smile == 7:
    print(f'{year}為馬年')
elif smile == 8:
    print(f'{year}為羊年')
elif smile == 9:
    print(f'{year}為猴年')
elif smile == 10:
    print(f'{year}為雞年')
elif smile == 11:
    print(f'{year}為狗年')
else:
    print(f'{year}為豬年')