from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    result = []
    if from_left == True:
        for dictionary in chainmap.maps:
            for k, v in dictionary.items():
                if k == key:
                    result.append(v)

    elif from_left == False:
        for dictionary in reversed(chainmap.maps):
            for k, v in dictionary.items():
                if k == key:
                    result.append(v)

    if result == []:
        return None
    else:
        return result[0]
