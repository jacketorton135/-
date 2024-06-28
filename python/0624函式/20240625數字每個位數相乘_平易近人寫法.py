user = input()

user = list(user)

data = []
for i in user:
    data.append(int(i))

result = 1

for j in data:
    result *= j

print(result)