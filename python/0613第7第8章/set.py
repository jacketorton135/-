a = {1, 2, 3}
print(type(a))
a = set()  # 建立空的set
print(type(a))

# 新增
a.add('d')
a.add(5)
a.add(5)
a.add(5)

print(a)

# 讀取
for i in a:
    print(i)

# 修改


# 刪除
a.remove(5)
print(a)