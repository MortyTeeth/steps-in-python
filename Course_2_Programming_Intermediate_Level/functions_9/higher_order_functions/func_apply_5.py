def func_apply(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def add3(x):
    return x + 3


def mul7(x):
    return x * 7
