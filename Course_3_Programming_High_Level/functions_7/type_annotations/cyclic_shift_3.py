def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step > 0:
        for i in range(step):
            elem = numbers[-1]
            del numbers[-1]
            numbers.reverse()
            numbers.append(elem)
            numbers.reverse()

        return None

    elif step == 0:
        return None

    else:
        for i in range(abs(step)):
            elem = numbers[0]
            del numbers[0]
            numbers.append(elem)
        return None
