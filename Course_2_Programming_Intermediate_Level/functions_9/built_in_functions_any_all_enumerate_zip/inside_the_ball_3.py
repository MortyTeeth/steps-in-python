def inside_the_ball(abscissas, ordinates, applicates):
    coordinates_of_points = list(zip(abscissas, ordinates, applicates))
    R = 2
    for_check = []
    for i in range(len(coordinates_of_points)):
        for abscissas, ordinates, applicates in coordinates_of_points:
            if (float(abscissas) ** 2 + float(ordinates) ** 2 + float(applicates) ** 2) > R ** 2:
                return False
            for_check.append(True)

    if all(for_check) is True:
        return True
    else:
        return False


abscissas = input().split()
ordinates = input().split()
applicates = input().split()
print(inside_the_ball(abscissas, ordinates, applicates))
