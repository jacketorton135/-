a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 一般寫法
new_list = []
for b in a:
    new_list.append(b + 10)
print(new_list)

# for comprehension寫法
new_list = [b + 10 for b in a]
print(new_list)