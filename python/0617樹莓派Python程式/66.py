6.
def fun1():
for i in range (2,7,2):
   		for j in range (2,7,2):
			result = i*j
			if result % 10 == 4 :
				print('我不喜歡數字四')
			else:
				print(f’{i}x{j}={result}’)
fun1()

