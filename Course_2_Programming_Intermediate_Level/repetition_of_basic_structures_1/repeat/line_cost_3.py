s = input()
count = 0

for i in range(len(s)):
    count += 1

price = count * 60

print(price // 100, 'р.', price % 100, 'коп.')