from datetime import datetime, date, timedelta


def employees_of_the_organization(count):
    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

    dict_with_employees = dict()
    for i in range(count):
        employee = input().split(' ')
        dict_with_employees.update({employee[0] + ' ' + employee[1]: datetime.strptime(employee[2], '%d.%m.%Y')})

    min_date = min([i for i in dict_with_employees.values()])

    count_employee_with_min_date = 0

    for key, value in dict_with_employees.items():
        if value == min_date:
            count_employee_with_min_date += 1

    if count_employee_with_min_date == 1:
        print(min_date.strftime('%d.%m.%Y'), get_key(dict_with_employees, min_date))
    else:
        print(min_date.strftime('%d.%m.%Y'), count_employee_with_min_date)


count_employees = int(input())

employees_of_the_organization(count_employees)
