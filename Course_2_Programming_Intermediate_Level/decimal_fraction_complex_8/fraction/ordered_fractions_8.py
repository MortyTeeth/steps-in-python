from math import gcd
from fractions import Fraction


def ordered_fractions(n):
    all_fractions = []
    for i in range(1, n + 1):
        for k in range(n, 1, -1):
            if gcd(i, k) == 1 and i < k:
                all_fractions.append(Fraction(i, k))
    fractions = sorted(all_fractions)

    for l in range(len(fractions)):
        print(fractions[l])


natural_number = int(input())

ordered_fractions(natural_number)
