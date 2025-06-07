def number_of_matching_pairs(string):
    list_with_symbols = string.split()
    list_with_nums = [int(i) for i in list_with_symbols]
    counter = 0
    for i in range(len(list_with_nums)):
        for j in range(i + 1, len(list_with_nums)):
            if list_with_nums[i] == list_with_nums[j]:
                counter += 1
    return counter


string_with_numbers = input()
print(number_of_matching_pairs(string_with_numbers))