from collections import Counter


def cost_of_the_course(products):
    list_with_products_and_nums = Counter(products)
    sorted_list = dict(sorted(list_with_products_and_nums.items(), key=lambda x: x[0]))
    max_len = max(len(product) for product in sorted_list)

    for product, num in sorted_list.items():
        product_without_spaces = ''.join([i for i in product if i != ' '])
        sum_product = sum(ord(i) for i in product_without_spaces)
        print(f'{product.ljust(max_len)}: {sum_product} UC x {num} = {sum_product * num} UC')


products = input().split(',')

cost_of_the_course(products)
