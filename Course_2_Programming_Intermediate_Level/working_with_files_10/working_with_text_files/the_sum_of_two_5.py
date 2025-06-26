sum_num2 = open('nums.txt', 'r', encoding='utf-8')
print(sum(int(i) for i in sum_num2.read().split()))
sum_num2.close()
