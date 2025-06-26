full_sum = open('prices.txt', 'r', encoding='utf-8')
sum = 0
list_with_all = full_sum.read().split()

l = []

for price_index in range(2, len(list_with_all) + 1, 3):
    l.append([list_with_all[price_index], list_with_all[price_index - 1], list_with_all[price_index - 2]])

for order in l:
    sum += int(order[0]) * int(order[1])
print(sum)
full_sum.close()
