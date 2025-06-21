def unique_symbols_2(num):
    mas = ''

    for i in range(num):
        l = input()
        a = l.lower()
        mas += a

    print(len(set(mas)))


numbers = int(input())

unique_symbols_2(numbers)