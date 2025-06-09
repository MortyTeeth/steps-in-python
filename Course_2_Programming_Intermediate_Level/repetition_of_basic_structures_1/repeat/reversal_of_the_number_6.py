def razvorot_na360(n):
    l = []
    l2 = ''
    l3 = []
    final = ''

    if len(n) == 5:
        for i in range(len(n)):
            l.append(int(n[i]))

        revers = l[::-1]

        while revers[0] == 0:
            del revers[0]

        for j in range(len(revers)):
            l2 += str(revers[j])

        return l2

    elif len(n) == 6:
        a = int(n) // 100000

        for k in range(len(n)):
            l3.append(int(n[k]))

        del l3[0]

        d = l3[::-1]

        prefinal = [a] + d

        for z in range(len(prefinal)):
            final += str(prefinal[z])

        return final


num = input()

print(razvorot_na360(num))
