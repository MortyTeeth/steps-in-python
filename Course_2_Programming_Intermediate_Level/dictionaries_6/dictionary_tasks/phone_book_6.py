my_dict = {}

for i in range(int(input())):
    value, key = input().lower().split()
    my_dict[key] = my_dict.get(key, []) + [value]

for k in range(int(input())):
    name = input().lower()
    print(*my_dict.get(name, ['абонент не найден']))
