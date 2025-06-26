with open('input.txt', 'r', encoding='utf-8') as input, open('output.txt', 'w', encoding='utf-8') as output:
    inp = [i for i in input.readlines()]
    for i, line in enumerate(inp, start=1):
        print((str(i) + ') ' + str(line)).rstrip(), file=output)
