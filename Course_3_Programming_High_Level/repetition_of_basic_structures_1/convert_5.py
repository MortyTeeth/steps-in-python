def convert(string):
    count_small_char = 0
    count_big_char = 0
    for char in string:
        if char.islower():
            count_small_char += 1
        elif char.isupper():
            count_big_char += 1

    if count_big_char > count_small_char:
        return string.upper()
    elif count_big_char == count_small_char:
        return string.lower()
    else:
        return string.lower()
