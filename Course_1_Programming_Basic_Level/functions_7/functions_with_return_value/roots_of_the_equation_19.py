import math


def solve(a, b, c):
    D = math.pow(b, 2) - (4 * a * c)

    if (D > 0):
        x_1 = (-b - math.sqrt(D)) / (2 * a)
        x_2 = (-b + math.sqrt(D)) / (2 * a)
        if (x_1 != x_2) and (a != 0):
            if (x_1 < x_2):
                return x_1, x_2
            else:
                return x_2, x_1
    elif (D == 0):
        x_2 = (-b + math.sqrt(D)) / (2 * a)
        x_1 = x_2
        return x_1, x_2
    else:
        print('Нет корней')
    pass


a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)
