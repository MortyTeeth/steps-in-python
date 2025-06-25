def interesting_numbers(f_n, s_n):
    for i in range(f_n, s_n + 1):
        digits = [int(q) for q in str(i)]
        if all(map(lambda x: x != 0 and i % x == 0, digits)):
            print(i, end=' ')


first_num, second_num = int(input()), int(input())

interesting_numbers(first_num, second_num)
