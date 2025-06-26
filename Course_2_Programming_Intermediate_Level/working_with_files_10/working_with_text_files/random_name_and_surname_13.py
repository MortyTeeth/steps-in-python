from random import *

with open('first_names.txt', 'r') as names, open('last_names.txt', 'r') as l_names:
    name, l_name = names.readlines(), l_names.readlines()
    print(choice(name).strip(), end=' ')
    print(choice(l_name).strip())
    print(choice(name).strip(), end=' ')
    print(choice(l_name).strip())
    print(choice(name).strip(), end=' ')
    print(choice(l_name).strip())
