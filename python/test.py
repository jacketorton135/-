import random

# 設置種子以確保可重複性
random.seed(42)

# 生成一個隨機浮點數
print(f"Random float between 0.0 and 1.0: {random.random()}")

# 生成一個隨機整數
print(f"Random integer between 1 and 10: {random.randint(1, 10)}")

# 生成一個隨機浮點數
print(f"Random float between 1.0 and 10.0: {random.uniform(1.0, 10.0)}")

# 從列表中隨機選擇一個元素
my_list = [1, 2, 3, 4, 5]
print(f"Random choice from list: {random.choice(my_list)}")

# 從列表中隨機選擇 3 個元素（可以重複）
print(f"Random choices from list: {random.choices(my_list, k=3)}")

# 從列表中隨機選擇 3 個不重複的元素
print(f"Random sample from list: {random.sample(my_list, 3)}")

# 原地打亂列表的順序
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")

# 生成一個服從正態分佈的隨機浮點數
print(f"Random Gaussian float with mu=0, sigma=1: {random.gauss(0, 1)}")