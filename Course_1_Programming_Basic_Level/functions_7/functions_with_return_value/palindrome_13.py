def is_palindrome(text):
    l = []
    b = text.lower()
    for i in range(len(b)):
        if b[i] not in ', . ! ? -':
            l.append(b[i])
    if l == l[::-1]:
        return True
    else:
        return False
    pass


txt = input()

print(is_palindrome(txt))
