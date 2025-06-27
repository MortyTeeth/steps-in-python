def same_parity(numbers):
    if numbers == []:
        return []
    elif numbers[0] % 2 == 0:
        numbers = [i for i in numbers if i % 2 == 0]
        return numbers
    elif numbers[0] % 2 == 1:
        numbers = [i for i in numbers if i % 2 == 1]
        return numbers
