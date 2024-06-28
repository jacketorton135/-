# # 將小於60的數字加上10
# new_list = [s + 10 if s < 60 else s for s in user_input]
# print(f'不及格加分: {new_list}')

new_list = [s + 10 if s < 60 else s for s in user_input]

print(new_list)