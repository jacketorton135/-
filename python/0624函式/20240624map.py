a = [13, 67, 34, 32, 98]

def dosomething(x):
    if x < 60:
        return x + 10
    else:
        return x

print(list(map(dosomething, a)))