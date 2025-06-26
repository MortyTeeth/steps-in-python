def concatenation_of_files(n):
    for i in range(n):
        file_name = input()
        with open(file_name, 'r', encoding='utf-8') as file, open('output.txt', 'a', encoding='utf-8') as output:
            output.write(file.read())


natural_num = int(input())

concatenation_of_files(natural_num)
