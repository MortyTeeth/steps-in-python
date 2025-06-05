num = int(input())

firstnum = num

sum = 0
colnum = 0
proiz = 1
lastnum = 0

while num != 0:
    b = num % 10
    sum = sum + b
    colnum = colnum + 1
    proiz = proiz * b
    num = num // 10
    if num != 0:
        lastnum = num

print(sum)
print(colnum)
print(proiz)
print(sum / colnum)
print(lastnum)
print(lastnum + firstnum % 10)