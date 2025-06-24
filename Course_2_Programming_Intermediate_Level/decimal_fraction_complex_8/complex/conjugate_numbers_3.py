def conjugate_numbers(n, f, s):
    ff = complex(f)
    ss = complex(s)
    print((ff ** n) + (ss ** n) + (ff ** (n)).conjugate() + (ss ** (n + 1)).conjugate())


natural_num, first_complex_num, second_complex_num = int(input()), input(), input()

conjugate_numbers(natural_num, first_complex_num, second_complex_num)
