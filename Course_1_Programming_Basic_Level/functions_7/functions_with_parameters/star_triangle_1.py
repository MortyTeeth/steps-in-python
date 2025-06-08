def draw_triangle(fill, base):
    count = 0
    for i in range(1, base):
        if base - base // 2 >= i:
            count += 1
            print(fill * i)
    for j in range(count + 1, base + 1):
        if base - base // 2 < i:
            count -= 1
            print(fill * (count))
    pass


fill = input()
base = int(input())

draw_triangle(fill, base)
