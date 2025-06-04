first = input()
second = input()
third = input()

long_1 = len(first)
long_2 = len(second)
long_3 = len(third)

max_long = max(long_1, long_2, long_3)
min_long = min(long_1, long_2, long_3)

if min_long == long_1:
    print(first)
if min_long == long_2:
    print(second)
if min_long == long_3:
    print(third)

if max_long == long_1:
    print(first)
if max_long == long_2:
    print(second)
if max_long == long_3:
    print(third)