def pluck(data, path, default=None):
    keys = path.split('.')

    for key in keys:
        if not isinstance(data, dict):
            return default
        data = data.get(key, default)

        if data == default:
            return default

    return data
