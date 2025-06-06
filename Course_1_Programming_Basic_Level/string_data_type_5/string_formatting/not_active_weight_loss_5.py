def not_active_weigh_lose(current_day, weight):
    the_weight_that_should_be = 100 - current_day * 0.2
    if the_weight_that_should_be >= weight:
        print('Все идет по плану')
        print(f'#{current_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {the_weight_that_should_be} кг')
    else:
        print('Что-то пошло не так')
        print(f'#{current_day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {the_weight_that_should_be} кг')


day = int(input())
current_weight = float(input())

not_active_weigh_lose(day, current_weight)