import json
from collections import ChainMap

with open('zoo.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)
    mapa = ChainMap(*data)
    c = 0

    for k, v in mapa.items():
        c += v
    print(c)
