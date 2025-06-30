def translate(alph, string):
    eng_aplh = 'abcdefghijklmnopqrstuvwxyz'
    tbl = str.maketrans(eng_aplh, alph)
    return string.translate(tbl)


alphabet = input()
string = input().lower()

print(translate(alphabet, string))
