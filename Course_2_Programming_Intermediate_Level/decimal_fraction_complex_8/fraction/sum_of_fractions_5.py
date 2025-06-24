from fractions import Fraction


def som_of_fractions(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / Fraction(i ** 2)

    print(Fraction(sum))


n = int(input())

som_of_fractions(n)
