def non_negative_even(numbers):
    if all(list(map(lambda x: True if x >= 0 else False, numbers))) and all(
            list(map(lambda x: True if x % 2 == 0 else False, numbers))):
        return True
    else:
        return False
