from math import gcd
from fractions import Fraction


def young_mathematician(n):
    all_fractions = []
    for i in range(1, n + 1):
        for k in range(n + 1, 1, -1):
            if gcd(i, k) == 1 and i + k == n and i < k:
                all_fractions.append(Fraction(i, k))
    print(max(all_fractions))


natural_number = int(input())

young_mathematician(natural_number)
