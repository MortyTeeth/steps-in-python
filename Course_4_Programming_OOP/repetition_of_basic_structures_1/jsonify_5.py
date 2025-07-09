import functools
import json


def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapper
