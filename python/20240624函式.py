def a():
    print('a')
    print('b')

print('c')

a() # 函式呼叫
a() # 函式呼叫
a() # 函式呼叫

def plus(a, b):  # 函式的參數式函式自己的私有變數(區域變數)
    if not isinstance(a, int):
        print('參數a不是數字')
    elif not isinstance(b, int):
        print('參數b不是數字')

    # a = 5
    # b = 6
    else:
        print(f'{a} + {b} = {a + b}')

plus(1, 3) # must
plus(13, 43) # must
plus(3, 's') # must