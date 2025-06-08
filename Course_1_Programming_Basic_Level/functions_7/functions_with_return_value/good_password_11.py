def is_password_good(password):
    l = []
    us1 = 0
    us2 = 0
    us3 = 0
    us4 = 0
    final = 0

    for i in range(len(password)):
        l.append(str(password[i]))

    if len(l) >= 8:  # us1
        us1 += 1

    for j in range(len(l)):
        if l[j].isupper() == True:
            us2 += 1
            break

    for n in range(len(l)):
        if l[n].islower() == True:
            us3 += 1
            break

    for o in range(len(l)):
        if l[o].isdigit() == True:
            us4 += 1
            break

    final = us1 + us2 + us3 + us4

    if final == 4:
        return True
    else:
        return False
    pass


txt = input()

print(is_password_good(txt))
