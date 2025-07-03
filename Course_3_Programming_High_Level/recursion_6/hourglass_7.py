def hourglass(counter, start_num, step, reverse=False):
    if counter == 0:
        return

    print(' ' * step + str(counter) * start_num)

    if reverse == False:
        if counter < 4:
            hourglass(counter + 1, start_num - 4, step + 2)
        else:
            hourglass(counter - 1, start_num + 4, step - 2, reverse=True)
    else:
        hourglass(counter - 1, start_num + 4, step - 2, reverse=True)


hourglass(1, 16, 0)
