import sys


def panoramic_agency():
    data = [line.strip() for line in sys.stdin.readlines()]
    data_with_lines = data[:-1]
    data_with_category = data[-1]

    lines_with_category = []
    for line in data_with_lines:
        if data_with_category in line:
            lines_with_category.append(line.split(' / '))

    sorted_list = sorted(lines_with_category, key=lambda x: (x[2], x[0]))

    for list_in in sorted_list:
        print(list_in[0])


panoramic_agency()
