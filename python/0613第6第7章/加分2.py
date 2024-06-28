user_input = []

for e in range(10000):
    score = input('請輸入成績(quit=離開): ')

    if score == 'quit':
        break
    else:
        user_input.append(int(score))

print(user_input)

# 處理成績
new_list = []

for s in user_input:
    if s < 60:
        new_list.append(s + 10)
    else:
        new_list.append(s)

# 使用單行if
new_list = []
for s in user_input:
    new_list.append(s + 10 if s < 60 else s)

new_list = [s + 10 if s < 60 else s for s in user_input]

print(new_list)