# filter

a = [3, '你', 99, 'abc', 87, 'X']

result = filter(lambda x: isinstance(x, int), a)

print(list(result))