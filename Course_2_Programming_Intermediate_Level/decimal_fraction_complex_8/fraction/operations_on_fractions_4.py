from fractions import Fraction


def operations_on_fractions(f_f, s_f):
    print(str(f_f) + ' + ' + str(s_f) + ' = ' + str(Fraction(f_f) + Fraction(s_f)))
    print(str(f_f) + ' - ' + str(s_f) + ' = ' + str(Fraction(f_f) - Fraction(s_f)))
    print(str(f_f) + ' * ' + str(s_f) + ' = ' + str(Fraction(f_f) * Fraction(s_f)))
    print(str(f_f) + ' / ' + str(s_f) + ' = ' + str(Fraction(f_f) / Fraction(s_f)))


first_fraction = input()
second_fraction = input()

operations_on_fractions(first_fraction, second_fraction)
