days_of_week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}


def get_weekday(number):
    if isinstance(number, int) != True:
        raise TypeError('Аргумент не является целым числом')
    if 7 < int(number) or int(number) < 1:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return days_of_week[number]
