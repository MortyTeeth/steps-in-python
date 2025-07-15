def hash_function(obj):
    str_obj = str(obj)
    first_iter = 0
    n = len(str_obj)

    for i in range(n // 2):
        first_iter += ord(str_obj[i]) * ord(str_obj[-i - 1])

    if n % 2 == 1:
        first_iter += ord(str_obj[n // 2])

    second_iter = 0
    value = 1
    for i in range(len(str_obj)):
        if i % 2 == 0:
            second_iter += ord(str_obj[i]) * value
            value += 1
        else:
            second_iter -= ord(str_obj[i]) * value
            value += 1

    result = (first_iter * second_iter) % 123456791

    return result
