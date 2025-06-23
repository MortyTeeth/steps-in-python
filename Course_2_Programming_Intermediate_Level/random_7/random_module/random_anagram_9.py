from random import *

word = input()

l = []

for i in range(len(word)):
    l.append(word[i])

shuffle(l)

for k in range(len(l)):
    print(l[k], end='')
