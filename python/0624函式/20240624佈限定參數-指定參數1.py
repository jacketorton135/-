def plus(*a):
    for i in a:
        print(i, end=' ')
    return sum(a)

print(plus(1, 2, 3, 4))

def showme(name, age, phone):
    print(f'姓名: {name}, 年紀: {age}, 電話: {phone}')

# 指定參數
showme(age=34, name='aaron', phone='0987654321')

# 第二種不定長度參數
def dosomething(**argv):
    print(argv)

dosomething(a=1, aaron=2, ok=3, w=4, aaa=5)