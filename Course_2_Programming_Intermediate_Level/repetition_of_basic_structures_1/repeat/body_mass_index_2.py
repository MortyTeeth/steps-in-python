def calc_mas(w, h):
    IMT = w / (h ** 2)
    if IMT > 25:
        return 'Избыточная масса'
    elif IMT < 18.5:
        return 'Недостаточная масса'
    else:
        return 'Оптимальная масса'


weight, height = float(input()), float(input())

print(calc_mas(weight, height))
