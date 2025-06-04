import math

a = float(input())
b = float(input())
c = float(input())

D = math.pow(b, 2) - (4 * a * c)

if (D >= 0):
    x_1 = (-b - math.sqrt(D)) / (2 * a)
    x_2 = (-b + math.sqrt(D)) / (2 * a)
    if (x_1 == x_2) and (a != 0):
            print (x_1)
    elif (x_1 != x_2) and (a != 0):
        if (x_1 < x_2):
            print(x_1)
            print(x_2)
        else:
            print(x_2)
            print(x_1)
else:
    print('Нет корней')