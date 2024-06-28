a = 1, 2, 3, # 打包

print(a, type(a))

c, d, e = a  # 解包

e, *f = a

print('e:', e)
print('f:', f)

a = 1,  2, 3, 4, 5

b, *c, d = a

print(b)
print(d)
print(c)