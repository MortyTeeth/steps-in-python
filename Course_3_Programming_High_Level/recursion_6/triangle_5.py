def triangle(num):
    try:
        if num != 0:
            print(num * '*')
            triangle(num - 1)
    except:
        pass
