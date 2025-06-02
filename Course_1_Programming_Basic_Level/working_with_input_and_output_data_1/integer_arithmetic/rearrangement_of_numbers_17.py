a = int(input())

print(a)
print(a // 100, a % 10, (a // 10) % 10, sep = "")
print((a // 10) % 10, a // 100, a % 10, sep = "")
print((a // 10) % 10, a % 10, a // 100, sep = "")
print(a % 10, a // 100, (a // 10) % 10, sep = "")
print(a % 10, (a // 10) % 10, a // 100, sep = "")