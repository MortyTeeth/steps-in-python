def countries_and_cities(n_c):
    dictionary = {}
    list_cities = []
    for i in range(n_c):
        line = input().split()
        dictionary.update({line[0]: line[1:]})

    num_cities = int(input())

    for k in range(num_cities):
        city = input()
        list_cities.append(city)

    for l in range(num_cities):
        for key, values in dictionary.items():
            if list_cities[l] in values:
                print(key)


num_country = int(input())

countries_and_cities(num_country)
