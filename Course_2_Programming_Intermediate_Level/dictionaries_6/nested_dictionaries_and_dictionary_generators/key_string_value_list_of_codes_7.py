words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {i: [ord(i[y]) for y in range(len(i))] for i in words}
