from functools import reduce

a = [23, 47, 98, 15, 62]

def dosomething(x, y):
    if x > y:
        return y
    else:
        return x

print(reduce(dosomething, a))