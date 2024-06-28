employee1 = {'英文', '日語', '粵語', '台語'}
employee2 = {'法文', '德語', '中文', '日語', '台語'}

print(f'兩個人都會的語言: {employee1 & employee2}')

print(f'兩個人總共會的語言: {employee1 | employee2}')

print(f'只有員工1會的語言: {employee1 - employee2}')
print(f'只有員工2會的語言: {employee2 - employee1}')

print(f'只有一個人會的語言: {employee1 ^ employee2}')