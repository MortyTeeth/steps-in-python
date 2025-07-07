def txt_to_dict():
    with open('planets.txt', 'r', encoding='UTF-8') as file:
        dict_with_planets = dict()
        lines = (line.strip() for line in file)
        for line in lines:
            if line != '':
                dict_with_planets.update({line.split(' = ')[0]: line.split(' = ')[1]})
            else:
                yield dict_with_planets
                dict_with_planets = dict()
        yield dict_with_planets
