with (open('lines.txt', 'r', encoding='utf-8')) as file:
    max_len_line = max(list(len(i.rstrip()) for i in file.readlines()))
    file.seek(0)
    for line in file:
        if len(line.strip()) == max_len_line:
            print(line.strip())
