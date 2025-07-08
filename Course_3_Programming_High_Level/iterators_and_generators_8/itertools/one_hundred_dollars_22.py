from itertools import combinations_with_replacement

wallet = [100, 50, 20, 10, 5]
len_wallet = len(wallet)
count = 0

for i in range(1, 21):
    iterator = set(combinations_with_replacement(wallet, i))
    for k in iterator:
        if sum(k) == 100:
            count += 1

print(count)
