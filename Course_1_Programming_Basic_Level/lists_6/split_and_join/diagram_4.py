s = input()

l = s.split()

plus = '+'

for i in range(len(l)):
    print(plus * int(l[i]), sep = '\n')