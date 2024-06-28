with open('code.txt', 'r', encoding='utf-8') as file_code, open('data.txt', 'r', encoding='utf-8') as file_data:
    code = file_code.readline()
    data = file_data.readline()

    print(code.replace('$data', data))

    eval(code.replace('$data', data))