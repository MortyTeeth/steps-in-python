def max_and_min(num):
    num_str = str(num)
    list_num = [int(i) for i in num_str]
    max_num = max(list_num)
    min_num = min(list_num)
    print('Максимальная цифра равна ' + str(max_num))
    print('Минимальная цифра равна ' + str(min_num))


number = int(input())

max_and_min(number)