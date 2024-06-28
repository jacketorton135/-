def b(func):
    def c(x, y):
        print('開始前執行')
        r = func(x, y)
        print('結束後執行')

        return r

    return c

@b
def a(x, y):
    print('很厲害的事情')

    return x + y


result = a(2, 3) # 其實就是變成呼叫c()函式

print(result)