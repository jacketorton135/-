# filter

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 50, 70, 80]

result = filter(lambda x: x >= 60, a)

print(list(result))