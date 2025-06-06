string = input()

first = string[0:string.find('h')]
second = string[string.rfind('h') + 1:]

print(first, second, sep = '')