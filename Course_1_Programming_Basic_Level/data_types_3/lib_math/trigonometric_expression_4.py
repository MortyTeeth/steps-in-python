import math

x = float(input())

a = math.sin(math.radians(x))
b = math.cos(math.radians(x))
c = math.tan(math.radians(x))
print(a + b + math.pow(c, 2))