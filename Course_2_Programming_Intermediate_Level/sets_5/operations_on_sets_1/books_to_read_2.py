def books_to_read(n, m, k, x, y, z, t, a):
    b = n + m - x - t
    c = m + k - y - t
    d = n + k - z - t

    f_b = n - t - b - d
    s_b = m - t - b - c
    t_b = k - t - d - c

    read_one_book = f_b + s_b + t_b
    read_two_book = b + c + d
    nothing_read = a - (f_b + s_b + t_b) - (b + c + d) - t

    print(read_one_book)
    print(read_two_book)
    print(nothing_read)


n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())
t = int(input())
a = int(input())

books_to_read(n, m, k, x, y, z, t, a)
