from collections import Counter


def income(nums):
    total_income = 0
    nums_counter = Counter(nums)
    number_of_buyers = int(input())
    list_with_clas_and_price = []
    for buyer in range(number_of_buyers):
        clas, price = input().split()
        list_with_clas_and_price.append([clas, price])

    for row in list_with_clas_and_price:
        if int(row[0]) in nums_counter.keys():
            total_income += int(row[1])
            hz = Counter({int(row[0]): 1})
            nums_counter = nums_counter - hz
    print(total_income)


numbers = [int(i) for i in input().split()]
income(numbers)
