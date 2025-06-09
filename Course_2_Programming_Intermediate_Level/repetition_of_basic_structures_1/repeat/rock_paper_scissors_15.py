def game(g1, g2):
    player1 = 'Тимур'
    player2 = 'Руслан'
    s1 = 'камень'
    s2 = 'бумага'
    s3 = 'ножницы'

    if g1 == g2:
        print('ничья')
    elif g1 == s1 and g2 == s2:
        print('Руслан')
    elif g1 == s1 and g2 == s3:
        print('Тимур')
    elif g1 == s2 and g2 == s1:
        print('Тимур')
    elif g1 == s2 and g2 == s3:
        print('Руслан')
    elif g1 == s3 and g2 == s1:
        print('Руслан')
    elif g1 == s3 and g2 == s2:
        print('Тимур')


g1 = input()
g2 = input()

game(g1, g2)