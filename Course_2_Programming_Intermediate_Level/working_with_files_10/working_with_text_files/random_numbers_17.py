from random import *

with open('random.txt', 'w', encoding='utf-8') as file:
    for i in range(25):
        file.writelines(str(randrange(111, 777)) + '\n')
