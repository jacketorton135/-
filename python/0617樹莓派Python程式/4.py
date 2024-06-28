#九九乘法表
for i in [ 2,4,6 ]:
    for j in [ 2,4,6]:
        print(f"{i} x {j} = {i*j:2d}\n", end='   ')
    print() #換行
