import json


def religions_and_countries():
    with open('countries.json', 'r', encoding='UTF-8') as countries:
        data = json.load(countries)
        relig = []
        for country in data:
            for key, value in country.items():
                if key == 'religion' and value not in relig:
                    relig.append(value)

    with open('religion.json', 'w', encoding='UTF-8') as religions:
        dictionary_with_countries_listed_by_religion = {}
        for country in data:
            for key, value in country.items():
                for rel in relig:
                    if rel in value:
                        if rel not in dictionary_with_countries_listed_by_religion:
                            dictionary_with_countries_listed_by_religion[rel] = []
                        dictionary_with_countries_listed_by_religion[rel].append(country["country"])
        religions.write(json.dumps(dictionary_with_countries_listed_by_religion, indent=3))


religions_and_countries()
