a = 0

while a < 3:
    print(a)
    a += 1

a = 1
while a < 10:
    print(f'2 x {a} = {a * 2}')
    a += 1

b = 1
while b < 10:
    a = 2
    while a < 10:
        print(f'{a} x {b} = {a * b}', end='\t')
        a += 1
    
    print()
    b += 1