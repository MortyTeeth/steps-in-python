def hide_card(c_n):
    for_del_space = ''
    for symbol in c_n:
        if symbol != ' ':
            for_del_space += symbol

    after_edit = '*' * 12 + for_del_space[-4:]
    return after_edit
