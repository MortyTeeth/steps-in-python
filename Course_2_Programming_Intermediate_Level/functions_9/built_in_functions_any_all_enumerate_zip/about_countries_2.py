countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

about_countries = zip(capitals, countries, population)

for i in range(6):
    for city, countries, population in about_countries:
        print(f'{city} is the capital of {countries}, population equal {population} people.')
