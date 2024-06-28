#九九乘法表
for i in [ 2,4,6 ]:
    for j in [ 2,4,6]:
       z=i*j
       if z==4: 
          print("我不喜歡數字四")
       elif z==24: 
          print("我不喜歡數字四")
       else: 
         print(f"{i} x {j} = {i*j:2d}\n", end='   ')
    print() #換行
