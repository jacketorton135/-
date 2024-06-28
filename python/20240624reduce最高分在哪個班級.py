from functools import reduce

a = {'甲': (31, 56, 23), '乙': (88, 92, 48), '丙': (100, 33, 72)}

# 找出班級最高分
def dosomething1(x, y):
    return x if x > y else y

def dosomething2(x, y):
    # 找出x班級最高分
    x1 = reduce(dosomething1, a[x])

    # 找出y班級最高分
    y1 = reduce(dosomething1, a[y])

    # 比較兩個班級的最高分
    if x1 > y1:
        return x  # 回傳班級名稱
    else:
        return y  # 回傳班級名稱
    
print(reduce(dosomething2, a))