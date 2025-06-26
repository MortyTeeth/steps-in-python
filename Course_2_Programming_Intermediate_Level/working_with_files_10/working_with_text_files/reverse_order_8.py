with (open('data.txt', 'r', encoding='utf-8')) as file:
    reverse = file.readlines()[::-1]
    for line in reverse:
        print(line.strip())
