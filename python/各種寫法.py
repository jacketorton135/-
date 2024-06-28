# 參與者名單
attendee = ['aaron', 'andy', 'apple', 'aaron', 'abner']

name = input('請輸入要查找的人名: ')

new_list = []

if name in attendee:
    print('有參加')
else:
    print('無參加')

if name in 'My name is aaron':
    print('有出現')
else:
    print('無出現')