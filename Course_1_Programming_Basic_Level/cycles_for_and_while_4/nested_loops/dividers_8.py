first_num = int(input())
second_num = int(input())

number_with_the_max_sum_of_divisors = 0
max_sum = 0
list_with_nums = []

for f in range(first_num, second_num + 1):
    sum_of_divisors = 0
    for s in range(1, f + 1):
        if f % s == 0:
            sum_of_divisors += s
    if sum_of_divisors > max_sum:
        max_sum = sum_of_divisors
        list_with_nums = [f]
    elif sum_of_divisors == max_sum:
        list_with_nums.append(f)

if len(list_with_nums) > 0:
    print(max(list_with_nums), max_sum)
else:
    print(number_with_the_max_sum_of_divisors, max_sum)
