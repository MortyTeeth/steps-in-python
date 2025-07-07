def simple_sequence():
    counter = 1
    while True:
        for i in range(counter):
            yield counter
        counter += 1
