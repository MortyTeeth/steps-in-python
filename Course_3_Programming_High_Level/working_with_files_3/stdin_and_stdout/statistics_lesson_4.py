import sys


def statistics_lesson():
    data = [int(i.strip()) for i in sys.stdin]
    if len(data) == 0:
        print('нет учеников')
    else:
        min_length = min(data)
        max_length = max(data)
        print(f'Рост самого низкого ученика: ' + str(min_length))
        print(f'Рост самого высокого ученика: ' + str(max_length))
        print(f'Средний рост:  ' + str(float(sum(data) / len(data))))


statistics_lesson()
