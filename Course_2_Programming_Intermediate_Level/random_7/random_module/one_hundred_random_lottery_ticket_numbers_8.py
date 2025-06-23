from random import *

list1 = []
list2 = []

for i in range(100):
    for_chek = randrange(1000000, 10000000)
    if for_chek not in list1:
        list1.append(for_chek)

list2 = sorted(list1)

for k in range(len(list2)):
    print(list2[k])
