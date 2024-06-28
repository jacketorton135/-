import copy

a = [1, 2, 3, 6, '嗨', True]

print(type(a), len(a))

# 新增資料
a.append('OK') # 從後面新增一筆資料
a.insert(0, 'KO')
a += ['99']  # a = a + ['99']
a.append([5, 6, 7])  # 在原本list內新增一筆list資料
a.extend([5, 6, 7])  # 將新的list資料打散接在原本list後面

print(a)

# 讀取
print(a[5])
print(a.pop())
# print(a[6])
print(a)

# 修改資料
a[0] = 'HH'

# 刪除
a.remove(6)  # 用資料本身來刪除
del a[0]     # 用位置刪除資料

# 複製list
b = a.copy()  # 複製內容
c = a         # 複製參考
d = copy.deepcopy(a)

a[0] = 999
b[1] = 888 
c[2] = 777
a[7][1] = 111

print(a)
print(b)
print(c)
print(d)

print(id(a), id(b), id(c), id(d))

print(a is b)
print(a is c)