def print_digit_sum(num):
    l = []
    a = str(n)
    b = a.split()

    count = 0
    for i in range(len(a)):
        count += 1
    for j in range(count):
        l.append(int(a[j]))

    print(sum(l))


n = int(input())

print_digit_sum(n)
