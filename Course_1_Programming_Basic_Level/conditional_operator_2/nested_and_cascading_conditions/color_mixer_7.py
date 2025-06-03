color_1 = input()
color_2 = input()

if (((color_1 == 'красный') and (color_2 == 'синий')) or ((color_1 == 'синий') and (color_2 == 'красный'))):
    print('фиолетовый')
elif (((color_1 == 'красный') and (color_2 == 'желтый')) or ((color_1 == 'желтый') and (color_2 == 'красный'))):
    print('оранжевый')
elif (((color_1 == 'желтый') and (color_2 == 'синий')) or ((color_1 == 'синий') and (color_2 == 'желтый'))):
    print('зеленый')
elif (color_1 == color_2 == 'красный'):
    print('красный')
elif (color_1 == color_2 == 'синий'):
    print('синий')
elif (color_1 == color_2 == 'желтый'):
    print('желтый')
else:
    print('ошибка цвета')