def is_valid_triangle(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return False
    else:
        return True
    pass


a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))