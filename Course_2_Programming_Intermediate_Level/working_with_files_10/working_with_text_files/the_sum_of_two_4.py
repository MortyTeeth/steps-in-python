sum_num = open('numbers.txt', 'r', encoding='utf-8')
print(sum(int(line.rstrip()) for line in sum_num.readlines()))
sum_num.close()
