def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    new_list = [i for i in elems if type(i) == int or type(i) == float]
    if len(new_list) < 1:
        return 0
    else:
        return sum(new_list)
