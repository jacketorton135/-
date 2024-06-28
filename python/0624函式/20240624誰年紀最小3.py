from functools import reduce

a = {'aaron': 13, 'andy': 45, 'apple': 22}

def dosomething(x, y):
    if a[x] > a[y]:
        return y
    else:
        return x
    
print(reduce(dosomething, a))