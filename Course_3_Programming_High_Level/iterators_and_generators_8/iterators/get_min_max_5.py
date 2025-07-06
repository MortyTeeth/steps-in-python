def get_min_max(data):
    if len(data) < 1:
        return None
    else:
        min_value = min(data)
        max_value = max(data)

        new_list = []

        for i in enumerate(data, start=0):
            if i[1] == min_value:
                new_list.append(i[0])
                break
        for i in enumerate(data, start=0):
            if i[1] == max_value:
                new_list.append(i[0])
                break
        return tuple(new_list)
