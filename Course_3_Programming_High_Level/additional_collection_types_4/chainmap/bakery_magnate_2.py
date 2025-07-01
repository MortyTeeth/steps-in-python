from collections import ChainMap
from collections import Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}


def bakery_magnate(list_product):
    mapa = ChainMap(bread, meat, sauce, vegetables, toppings)
    new_list_product = []
    total_cost = 0
    counter = Counter(list_product)
    length_num = max(counter.items(), key=lambda x: x[1])[1]
    sorted_counter = dict(sorted(counter.items(), key=lambda x: x[0]))
    max_len_product_name = len(max(sorted_counter.items(), key=lambda x: len(x[0]))[0])

    for key, value in sorted_counter.items():
        for tuple2 in mapa.items():
            tuple1 = dict({tuple2[0]: tuple2[1]})
            for dictionary_product, dictionary_price in tuple1.items():
                if key == dictionary_product:
                    new_list_product.append(f'{key.ljust(max_len_product_name, " ")} x {value}')
                    total_cost += value * dictionary_price
    print(*new_list_product, sep='\n')
    len_final_string = len(f'ИТОГ: {total_cost}р')
    if len_final_string > max_len_product_name:
        print((len_final_string) * '-')
    else:
        if length_num >= 10:
            print((max_len_product_name + 5) * '-')
        else:
            print((max_len_product_name + 4) * '-')
    print(f'ИТОГ: {total_cost}р')


products = input().split(',')
bakery_magnate(products)
