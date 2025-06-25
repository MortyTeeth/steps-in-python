athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

natural_num = int(input())


def return_by_number(athletes):
    def send_n_n(natural_num):
        return natural_num

    return send_n_n(athletes[natural_num - 1])


athletes.sort(key=return_by_number)

num = 0
for i in athletes:
    print(*athletes[num])
    num += 1
