nabor = input()

nabor2 = nabor.split()

nabor3 = []

for i in range(len(nabor2)):
    nabor3.append(int(nabor2[i]))

nabor4 = [nabor3[i] ** 3 for i in range(len(nabor3))]

print(*nabor4)