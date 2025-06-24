def string_representation(num):
    split_num = list(str(num))
    numbers_and_naming = {0: 'zero',
                          1: 'one',
                          2: 'two',
                          3: 'three',
                          4: 'four',
                          5: 'five',
                          6: 'six',
                          7: 'seven',
                          8: 'eight',
                          9: 'nine'}

    for i in range(len(split_num)):
        if int(split_num[i]) in numbers_and_naming.keys():
            if int(split_num[i]) != len(numbers_and_naming):
                print(numbers_and_naming[int(split_num[i])], end=' ')
            else:
                print(numbers_and_naming[int(split_num[i])], sep='')


number = int(input())

string_representation(number)
