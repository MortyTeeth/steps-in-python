from fractions import Fraction


def reduce_the_fraction(m, n):
    str_m = str(m)
    str_n = str(n)

    str_all = str_m + '/' + str_n

    print(Fraction(str_all))


m, n = int(input()), int(input())

reduce_the_fraction(m, n)
