year = int(input('請輸入民國年: '))
print(f'民國{year}年 = 西元{year+1911}年')

smile = year % 12

match smile:
    case 1:
        print(f'{year}為鼠年')
    case 2:
        print(f'{year}為牛年')
    case 3:
        print(f'{year}為虎年')
    case 4:
        print(f'{year}為兔年')
    case 5:
        print(f'{year}為龍年')
    case 6:
        print(f'{year}為蛇年')
    case 7:
        print(f'{year}為馬年')
    case 8:
        print(f'{year}為羊年')
    case 9:
        print(f'{year}為猴年')
    case 10:
        print(f'{year}為雞年')
    case 11:
        print(f'{year}為狗年')
    case 0:
        print(f'{year}為豬年')
    case _:
        print('發生錯誤')