english_symbols = 'AaBCcEeHKMOoPpTXxy'
russian_symbols = 'АаВСсЕеНКМОоРрТХху'

count = 0
for i in range(3):
    symbol = input()
    if symbol in english_symbols:
        count += 1
    else:
        count -= 1
if count == 3:
    print('en')
elif count == -3:
    print('ru')
else:
    print('mix')
