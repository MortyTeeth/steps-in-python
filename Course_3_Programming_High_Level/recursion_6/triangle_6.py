def triangle(num):
    try:
        if num != 0:
            triangle(num - 1)
            print(num * '*')
    except:
        pass
