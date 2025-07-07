def alternating_sequence(x=None):
    if x == None:
        counter = 1
        while True:
            if counter % 2 == 1:
                yield counter
                counter += 1
            else:
                yield -counter
                counter = counter + 1
    else:
        for i in range(1, 1 + x):
            if i % 2 == 1:
                yield i
            else:
                yield -i
