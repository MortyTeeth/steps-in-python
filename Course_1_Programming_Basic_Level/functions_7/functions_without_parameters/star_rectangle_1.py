def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            print(10 * '*')
        else:
            print('*', 8 * ' ', '*', sep='')
    pass


draw_box()
