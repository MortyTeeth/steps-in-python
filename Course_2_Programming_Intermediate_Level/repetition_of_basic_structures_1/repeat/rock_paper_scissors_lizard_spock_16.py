first_player = 'Тимур'
second_player = 'Руслан'

signs_and_index = {'камень': 1, 'ящерица': 2, 'Спок': 3, 'ножницы': 4, 'бумага': 5}


def small_game(first_p, second_p):
    if signs_and_index[first_p] == signs_and_index[second_p]:
        print('ничья')
    elif abs(signs_and_index[first_p] - signs_and_index[second_p]) % 2 == 0:
        print(second_player) if signs_and_index[second_p] > signs_and_index[first_p] else print(first_player)

    elif abs(signs_and_index[first_p] - signs_and_index[second_p]) % 2 == 1:
        print(first_player) if signs_and_index[second_p] > signs_and_index[first_p] else print(second_player)


small_game(input(), input())
