def sort_by_column(num):
    with open('deniro.csv', 'r', encoding='UTF-8') as file:
        data = file.read()
        rows = [r.split(',') for r in data.splitlines()]

        if num == 1:
            sorted_list = sorted(rows, key=lambda x: x[num - 1])
        elif num == 2:
            sorted_list = sorted(rows, key=lambda x: int(x[num - 1]))
        else:
            sorted_list = sorted(rows, key=lambda x: int(x[num - 1]))

        for row in sorted_list:
            print(f'{row[0]},{row[1]},{row[2]}')


number = int(input())

sort_by_column(number)