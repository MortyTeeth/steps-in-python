def without_cycles(num):
    if num > 0:
        print(num)
        without_cycles(num - 5)
        print(num)
    else:
        print(num)


number = int(input())
without_cycles(number)
