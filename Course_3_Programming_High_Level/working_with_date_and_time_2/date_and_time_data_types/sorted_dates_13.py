from datetime import date


def sorted_dates(c_d):
    dictionary = []
    for i in range(c_d):
        year, month, day = input().split('-')
        first_date = date(int(year), int(month), int(day))
        dictionary.append(first_date)
    sorted_dictionary = sorted(dictionary)
    for dat in sorted_dictionary:
        print(dat.strftime('%d/%m/%Y'))


count_date = int(input())
sorted_dates(count_date)
