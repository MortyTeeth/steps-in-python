def evaluate(coefficients, x):
    list_of_coefficients = [int(i) for i in coefficients]
    sum = 0
    for i in range(len(list_of_coefficients) - 1, -1, -1):
        if x ** i == 0:
            sum += list_of_coefficients[len(list_of_coefficients) - (i + 1)]
        else:
            sum += list_of_coefficients[len(list_of_coefficients) - (i + 1)] * (x ** i)

    return sum


coefficients, x = input().split(), int(input())

print(evaluate(coefficients, x))
