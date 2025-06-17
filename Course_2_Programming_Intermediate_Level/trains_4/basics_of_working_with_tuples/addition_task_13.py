new_tuples = []
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
for i in range(len(tuples)):
    vr = list(tuples[i])
    vr[-1] = 100
    new_tuples.append(tuple(vr))
print(new_tuples)