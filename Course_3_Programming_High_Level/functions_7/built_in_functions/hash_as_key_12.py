def hash_as_key(objects):
    dictionary = {}

    for i in objects:
        h = hash(i)

        if h in dictionary:
            if isinstance(dictionary[h], list):
                dictionary[h].append(i)
            else:
                dictionary[h] = [dictionary[h], i]
        else:
            dictionary[h] = i

    return dictionary
