n = int(input())

factorial = 1

sum = 0

for i in range(1, n+1):
    factorial *= i
    sum = sum + factorial
print(sum)