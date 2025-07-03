list_tribonacci = [1, 1, 1]


def tribonacci(number):
    list_tribonacci.append(sum(list_tribonacci[-3:]))
    if len(list_tribonacci) < number + 1:
        return tribonacci(number)
    return list_tribonacci[number - 1]
