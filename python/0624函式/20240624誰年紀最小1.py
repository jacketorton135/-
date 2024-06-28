from functools import reduce

a = [1, 2, 3, 4, 5, 6]

def dosomething(x, y):
    return x + y

print(reduce(dosomething, a))