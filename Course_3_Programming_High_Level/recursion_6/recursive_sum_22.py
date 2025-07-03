def recursive_sum(nested_lists, summa=0):
    try:
        for i in nested_lists:
            if isinstance(i, int):
                summa += i
            elif isinstance(i, list):
                summa = recursive_sum(i, summa)
        return summa
    except:
        pass
