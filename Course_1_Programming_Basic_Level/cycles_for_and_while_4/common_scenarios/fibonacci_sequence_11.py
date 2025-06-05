n = int(input())
f_1 = 1
f_2 = 1

if n > 1:
    print(f_1, f_2, end = ' ')
    for i in range(2, n):
        f_1, f_2 = f_2, f_1 + f_2
        print(f_2, end = ' ')
else:
    print(1)