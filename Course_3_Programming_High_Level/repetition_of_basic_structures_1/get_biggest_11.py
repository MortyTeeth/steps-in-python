def get_biggest(numbers):
    if len(numbers) != 0:
        max_len = max([len(str(i)) for i in numbers])
        gluing = ''
        after_sorted = sorted(numbers, key=lambda x: str(x) * max_len, reverse=True)
        if any(True for i in numbers if i != 0):
            for i in after_sorted:
                gluing += str(i)
            return gluing
        return 0
    else:
        return -1
