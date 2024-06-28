# import busytuesday

# r = busytuesday.mux(4, 5)
# print('同事的結果:', r)
# print('同事的結果:', busytuesday.owner)

from busytuesday import div

# 衝突
# def div():
#     print('同名函式')

result = div(6, 3)
print(result)