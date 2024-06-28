school = [43, 52, 26, 33, 91, 5, 11]
a = [78, 63, 45, 88, 37, 92]

from functools import reduce

# 找出班級最低分
min = reduce(lambda x, y: y if x > y else x, a)
print(f'最低分: {min}')

total = reduce(lambda x, y: x + y, school)
avg = total / len(school)
print(f'全校平均: {avg:2.2f}')

if avg > min:
    print('該班級最低分低於全校平均')
elif avg < min:
    print('該班級最低分高於全校平均')
else:
    print('該班級最低分等於全校平均')