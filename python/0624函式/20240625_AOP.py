def b(func):
    def c():
        print('開始前執行')
        func()
        print('結束後執行')

    return c

@b
def a():
    print('很厲害的事情')
    
    return 999