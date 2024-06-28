#def foo():
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9

g = foo()

a = [11, 22, 33]

b = (i for i in a)

print(next(b))
print(next(b))
print(next(b))