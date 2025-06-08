def is_valid_password(password):
    count = 0
    d = 0
    e = 0
    ch = []
    l = psw.split(':')
    for i in range(len(l)):
        ch.append(int(l[i]))
        d += 1

    firstch = ch[0]
    secondch = ch[1]
    thirdch = ch[2]
    if str(firstch) == str(firstch)[::-1]:
        count += 1

    for i in range(1, secondch + 1):
        if secondch % i == 0 and secondch != 0:
            e += 1
        else:
            e = e
    if e == 2:
        count += 1

    if thirdch % 2 == 0:
        count += 1

    if count == 3 and d == 3:
        return True
    else:
        return False

    pass


psw = input()

print(is_valid_password(psw))
