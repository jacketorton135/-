def math(a, b, f):
    return f(a, b)

def plus(a, b):
    return a + b

def mux(a, b):
    return a * b

a = math(2, 3, plus)
print(a)

a = math(2, 3, mux)
print(a)