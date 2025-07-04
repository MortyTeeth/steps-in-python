names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]


def cartoon_profit():
    list_with_cartoon_and_profit = list(zip(names, budgets, box_offices))
    sorted_list = sorted(list_with_cartoon_and_profit, key=lambda x: x[0])
    for cartoon in sorted_list:
        print(f'{cartoon[0]}: {cartoon[2] - cartoon[1]}$')


cartoon_profit()
