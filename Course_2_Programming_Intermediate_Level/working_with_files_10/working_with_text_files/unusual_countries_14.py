with open('population.txt', 'r', encoding='utf-8') as file:
    result = [i.split() for i in file.readlines()]
    for country in result:
        if country[0][0] == 'G' and int(country[-1]) > 500000:
            print(country[0])
