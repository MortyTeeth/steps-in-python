with open('class_scores.txt', 'r', encoding='utf-8') as past, open('new_scores.txt', 'w', encoding='utf-8') as new:
    list_before_plus_5 = [i.strip().split() for i in past.readlines()]
    for sec_name, mark in list_before_plus_5:
        if int(mark) > 94:
            print(sec_name, str(100), file=new)
        else:
            print(sec_name, str(int(mark) + 5), file=new)
