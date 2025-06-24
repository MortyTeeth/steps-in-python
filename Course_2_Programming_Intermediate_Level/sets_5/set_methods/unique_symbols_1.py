def unique_symbols_1(num):
    mas = []

    for i in range(num):
        l = input()
        a = l.lower()
        m = set(a)
        mas.append(m)

    for k in range(num):
        print(len(set(mas[k])))


numbers = int(input())

unique_symbols_1(numbers)