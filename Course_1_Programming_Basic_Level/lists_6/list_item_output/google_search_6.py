def filling_out_the_first_list(numbers_of_lines_1):
    first_list = []
    for i in range(numbers_of_lines_1):
        string = input()
        first_list.append(string)

    return first_list


def filling_out_the_second_list(numbers_of_lines_2):
    second_list = []
    for k in range(numbers_of_lines_2):
        string = input()
        second_list.append(string)

    return second_list


def check_availability(first_list, second_list):
    list_with_the_necessary_lines = []
    for string in first_list:
        counter = 0
        len_list2 = len(second_list)
        for string_for_check in second_list:
            if string_for_check.lower() in string.lower():
                counter += 1
                if len_list2 == counter:
                    list_with_the_necessary_lines.append(string)

    for n in list_with_the_necessary_lines:
        print(n)


numbers_of_lines1 = int(input())
first_list = filling_out_the_first_list(numbers_of_lines1)

numbers_of_lines2 = int(input())
second_list = filling_out_the_second_list(numbers_of_lines2)

check_availability(first_list, second_list)