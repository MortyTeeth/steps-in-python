def eng_alph(char):
    if ord(char) < ord('z'):
        print(char)
        eng_alph(chr(ord(char) + 1))
    else:
        print(char)


eng_alph('a')
