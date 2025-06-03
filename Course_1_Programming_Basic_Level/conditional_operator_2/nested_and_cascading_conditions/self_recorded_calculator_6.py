number_1 = int(input())
number_2 = int(input())
string = input()

if string == '/':
    if number_2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(number_1 / number_2)
elif string == '*':
    print(number_1 * number_2)
elif string == '+':
    print(number_1 + number_2)
elif string == '-':
    print(number_1 - number_2)
else:
    print('Неверная операция')