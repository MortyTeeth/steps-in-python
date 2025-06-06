num1 = int(input())
num2 = int(input())

string1 = 'Для чисел {0} и {1}:'.format(num1, num2)
string2 = '  Сумма кубов: {0}**3 + {1}**3 = {2}'.format(num1, num2, (num1 ** 3 + num2 ** 3))
string3 = '  Куб суммы: ({0} + {1})**3 = {2}'.format(num1, num2, (num1 + num2) ** 3)

print(string1)
print(string2)
print(string3)