def fun1():
    for i in range(2,7,2):
        for j in range(2,7,2):
            if(i*j==4 or i*j==24):
                print("我不喜歡數字四")
            else:
                print(f"{i}*{j}={i*j}")
    print("\b ")


fun1()
