def convert_to_python_case(text):
    l = []
    for j in range(len(text)):
        l.append(text[j])

    for j in range(1, len(l)):
        if l[j].isupper() == True:
            l[j - 1] += '_'
    a = ''.join(l)

    return a.lower()

    pass


txt = input()

print(convert_to_python_case(txt))
