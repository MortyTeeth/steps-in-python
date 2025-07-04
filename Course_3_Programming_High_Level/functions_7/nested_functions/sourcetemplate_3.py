def sourcetemplate(url):
    def load(**kwargs):
        if len(kwargs) < 1:
            return url
        else:

            return url + '?' + '&'.join(sorted([str(key) + '=' + str(value) for key, value in kwargs.items()]))

    return load
