def greet(name, *args):
    if len(args) == 0:
        return ('Hello, ' + name + '!')
    else:
        return ('Hello, ' + name + ' and ' + ' and '.join(args) + '!')
