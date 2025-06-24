dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}

for key in dict1:
    if key in dict2:
        result.update({key: dict1[key] + dict2[key]})
    else:
        result.update({key: dict1[key]})


for key in dict2:
    if key not in result:
        result.update({key: dict2[key]})
