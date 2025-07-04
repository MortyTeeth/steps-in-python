def max_and_min():
    list_with_func_result = []
    func = input()
    a, b = [int(i) for i in input().split()]

    for x in range(a, b + 1):
        list_with_func_result.append(eval(func))

    print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min(list_with_func_result)}')
    print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max(list_with_func_result)}')


max_and_min()
