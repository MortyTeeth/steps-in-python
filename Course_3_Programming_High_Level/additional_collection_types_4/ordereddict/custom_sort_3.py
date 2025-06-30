def custom_sort(ordered_dict, by_values=False):
    sorted_items = sorted(ordered_dict.items(), key=lambda x: x[1] if by_values else x[0])
    ordered_dict.clear()
    ordered_dict.update(sorted_items)
