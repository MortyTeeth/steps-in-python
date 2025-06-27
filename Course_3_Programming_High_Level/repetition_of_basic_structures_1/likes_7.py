def likes(names):
    if len(names) == 0:
        return 'Никто не оценил данную запись'
    elif len(names) == 1:
        return str(names[0]) + ' оценил(а) данную запись'
    elif len(names) == 2:
        return str(names[0]) + ' и ' + str(names[1]) + ' оценили данную запись'
    elif len(names) == 3:
        return str(names[0]) + ', ' + str(names[1]) + ' и ' + str(names[2]) + ' оценили данную запись'
    else:
        return str(names[0]) + ', ' + str(names[1]) + ' и ' + str(len(names) - 2) + ' других оценили данную запись'
