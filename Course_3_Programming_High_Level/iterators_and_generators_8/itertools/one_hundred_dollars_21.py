from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
len_wallet = len(wallet)
count = 0

for i in range(1, len(wallet) + 1):
    iterator = set(combinations(wallet, i))
    for k in iterator:
        if sum(k) == 100:
            count += 1

print(count)
