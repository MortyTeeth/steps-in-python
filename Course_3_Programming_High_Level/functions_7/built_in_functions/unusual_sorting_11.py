def unusual_sorting(line):
    small_symbols = [i for i in line if i.islower()]
    small_symbols_sorted = sorted(small_symbols)
    small = ','.join(small_symbols_sorted).replace(',', '')

    big_symbols = [i for i in line if i.isupper()]
    big_symbols_sorted = sorted(big_symbols)
    big = ','.join(big_symbols_sorted).replace(',', '')

    digits = [i for i in line if i.isdigit()]
    odd_numbers = [i for i in digits if int(i) % 2 == 1]
    sorted_odd = sorted(odd_numbers)
    odd = ','.join(sorted_odd).replace(',', '')

    even_numbers = [i for i in digits if int(i) % 2 == 0]
    sorted_even = sorted(even_numbers)
    even = ','.join(sorted_even).replace(',', '')

    print(small + big + odd + even)


string = input()
unusual_sorting(string)
