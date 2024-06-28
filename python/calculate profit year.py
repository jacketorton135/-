# 寫法一
year = int(input('請輸入年份: '))

if year % 400 == 0:
    print('潤年')
elif year % 4 == 0 and year % 100 != 0:
    print('潤年')
else:
    print('平年')

# 寫法二
year = int(input('請輸入年份: '))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('潤年')
else:
    print('平年')
    
# 寫法三
print(f'{(year := int(input('請輸入年份: ')))}: {'潤年' if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else '平年'}')