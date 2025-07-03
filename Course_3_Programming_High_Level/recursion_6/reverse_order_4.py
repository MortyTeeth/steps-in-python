def reverse_order(num):
    if num != 0:
        reverse_order(int(input()))
        print(num)
    else:
        print(num)


reverse_order(int(input()))
