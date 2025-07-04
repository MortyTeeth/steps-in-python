def collections(non_empty_list):
    if isinstance(eval(non_empty_list), list):
        print(eval(non_empty_list)[-1])
    elif isinstance(eval(non_empty_list), tuple):
        print(eval(non_empty_list)[0])
    elif isinstance(eval(non_empty_list), set):
        print(len(eval(non_empty_list)))


non_empty_list = input()
collections(non_empty_list)
