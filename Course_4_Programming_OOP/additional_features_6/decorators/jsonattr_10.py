import json


def jsonattr(filename):
    def decorator(cls):
        with open(filename, "r") as file:
            templates = json.load(file)
            for k, v in templates.items():
                setattr(cls, k, v)
            return cls

    return decorator
