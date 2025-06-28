from datetime import datetime, date, timedelta


def employees_of_the_organization(count):
    dict_with_employees = dict()
    for i in range(count):
        employee = input().split(' ')
        if datetime.strptime(employee[2], '%d.%m.%Y') not in dict_with_employees:
            dict_with_employees.update({datetime.strptime(employee[2], '%d.%m.%Y'): 1})
        else:
            dict_with_employees.update({datetime.strptime(employee[2], '%d.%m.%Y'): dict_with_employees[
                                                                                        datetime.strptime(employee[2],
                                                                                                          '%d.%m.%Y')] + 1})

    max_count = max(dict_with_employees.values())
    list_with_date = []

    for key, value in dict_with_employees.items():
        if value == max_count:
            list_with_date.append(key)

    sorted_dates = sorted(list_with_date)

    for i in sorted_dates:
        print(i.strftime('%d.%m.%Y'))


count_employees = int(input())

employees_of_the_organization(count_employees)
