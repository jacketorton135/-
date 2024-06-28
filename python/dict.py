a = {'d': 8, 1: 99, True: 88, 33: 'OK', 0: 'aaron', False: 'andy', frozenset({3, 4}): 'hh'}

# a[4] = 99
# a[4] = 88
# del a[4]

# a[1] = 77

# print(a[True])
print(a)

for key in a:
    print(key, a[key])

for value in a.values():
    print(value)


# a = ['aaron', 'andy', 'apple']
# b = [44, 77, 9]

# print(dict(zip(a, b)))

print(a[ frozenset({3, 4})  ])

b = {4: 5}

a.update(b)

print(a)