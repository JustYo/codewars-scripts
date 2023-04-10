def find_max_sum(n):
    result = []
    a1 = 1
    a2 = 1
    a3 = 1
    if n == 0:
        result = 0
    else:
        result1 = 0
        result2 = 0
        for i in range(n):
            if a1 + a2 % 2 != 0:
                a1 = i
            if a2 + a3 % 3 != 0:
                a2 = i
            result = a1 + a2 + a3
    return result


print(find_max_sum(3))
