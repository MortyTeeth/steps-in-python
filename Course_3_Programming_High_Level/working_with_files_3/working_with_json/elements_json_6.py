import json
import sys


def elements_json():
    data = json.load(sys.stdin)

    for key, value in dict(data).items():
        if type(value) == list:
            print(f'{key}: {", ".join(map(str, value))}')
        else:
            print(f'{key}: {value}')


elements_json()
