a = ''
s = input()

l = s.split()
sl = ''.join(l)

hz = []
for i in range(len(sl)):
    hz.append(sl[i])

del hz[0]

colstrok = ''.join(hz)

realcolstrok = int(colstrok)

for j in range(realcolstrok):
    string = input()
    position = string.find('#')
    if position != -1:
        a = string[:position]
        print(a.rstrip())
    else:
        print(string)