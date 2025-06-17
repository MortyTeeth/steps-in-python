def vertex_of_parabola(a, b, c):
    first_vertex = ((-b) / (2 * a))
    second_vertex = (((4 * a * c) - (b ** 2)) / (4 * a))
    print((first_vertex, second_vertex))


a = int(input())
b = int(input())
c = int(input())

vertex_of_parabola(a, b, c)
