import json


def is_correct_json(string):
    try:
        data = json.loads(string)
        return 'True'
    except:
        return 'False'
