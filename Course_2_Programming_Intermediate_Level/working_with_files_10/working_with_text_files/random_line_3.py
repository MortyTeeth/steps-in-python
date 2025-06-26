from random import *

for_example = open('lines.txt', 'r', encoding='utf-8')
print(choice([line.strip() for line in for_example.readlines()]))
