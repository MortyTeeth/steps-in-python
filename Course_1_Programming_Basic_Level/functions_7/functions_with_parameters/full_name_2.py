def print_fio(name, surname, patronymic):
    for i in range(1):
        print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep = '')
    pass


name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)