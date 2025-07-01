from collections import Counter


def not_lazy(products):
    list_with_products_and_nums = Counter(products)
    sorted_list = dict(sorted(list_with_products_and_nums.items(), key=lambda x: x[0]))

    for product, num in sorted_list.items():
        print(f'{product}: {num}')


products = input().split(',')

not_lazy(products)
