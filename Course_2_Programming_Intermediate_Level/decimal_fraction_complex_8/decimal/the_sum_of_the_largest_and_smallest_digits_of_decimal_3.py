from decimal import *

num = Decimal(input())
num_tuple = num.as_tuple().digits

print((abs(num) >= 1) * min(num_tuple) + max(num_tuple))
