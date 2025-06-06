s = input()

most_common = s[0]
for el in s:
    if s.count(el) >= s.count(most_common):
        most_common = el

print(most_common)