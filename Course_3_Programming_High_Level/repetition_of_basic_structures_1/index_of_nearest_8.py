def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    else:
        list_abs = [abs(i - number) for i in numbers]
        return list_abs.index(min(list_abs))
