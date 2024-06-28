def kill_odd(data):
    # result = []

    # for i in data:
    #     if i % 2 == 0:
    #         result.append(i)

    # return result

    return [i for i in data if i % 2 == 0]

print(kill_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))