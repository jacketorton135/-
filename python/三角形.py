high = int(input("請輸入三角形的高度: "))
#定義每行三角形範圍
for i in range(1, high + 1):
#打印每行空格
    print(' ' * (high - i), end='')
 #打印美行的*號
    print('*' * (2 * i - 1))