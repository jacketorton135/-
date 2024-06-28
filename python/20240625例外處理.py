
print('1')

try:    
    [1, 2, 3][3]
    int('a')
except ValueError:
    print('轉型錯誤')
except IndexError:
    print('索引錯誤')

print('2')