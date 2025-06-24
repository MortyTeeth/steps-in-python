from fractions import Fraction
from math import *


def sum_of_fractions2(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / Fraction(factorial(i))

    print(Fraction(sum))


n = int(input())

sum_of_fractions2(n)
