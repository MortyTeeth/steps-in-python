list_with_nums = []


def to_binary(number):
    if number != 0:
        if number % 2 == 1:
            number = number // 2
            to_binary(number)
            list_with_nums.append(str(1))

        elif number % 2 == 0:
            number = number // 2
            to_binary(number)
            list_with_nums.append(str(0))

        result = ' '.join(list_with_nums)
        final_result = result.replace(' ', '')
        return final_result
    else:
        return 0
