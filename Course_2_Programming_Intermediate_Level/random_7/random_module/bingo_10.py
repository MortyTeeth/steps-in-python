from random import *

first_l = []
second_l = []
third_l = []
fourth_l = []
fifth_l = []

matrix = []

one = 0
two = 0
three = 0
four = 0
five = 0

while one < 5:
    first5 = randrange(1, 16)
    if first5 not in first_l:
        first_l.append(first5)
        one += 1
matrix.append(first_l)

while two < 5:
    second5 = randrange(16, 31)
    if second5 not in second_l:
        second_l.append(second5)
        two += 1
matrix.append(second_l)

while three < 5:
    third5 = randrange(31, 46)
    if third5 not in third_l:
        third_l.append(third5)
        three += 1
matrix.append(third_l)

while four < 5:
    fourth5 = randrange(46, 61)
    if fourth5 not in fourth_l:
        fourth_l.append(fourth5)
        four += 1
matrix.append(fourth_l)

while five < 5:
    fifth5 = randrange(61, 76)
    if fifth5 not in fifth_l:
        fifth_l.append(fifth5)
        five += 1
matrix.append(fifth_l)

matrix[2][2] = 0

full_reverse_matrix = []

for i in range(5):
    matrix_reverse = []
    for k in range(5):
        matrix_reverse.append(matrix[k][i])
    full_reverse_matrix.append(matrix_reverse)

space = 3

for i in range(len(full_reverse_matrix)):
    for k in range(len(full_reverse_matrix[i])):
        print(str(full_reverse_matrix[i][k]).ljust(space), end='')
    print()
