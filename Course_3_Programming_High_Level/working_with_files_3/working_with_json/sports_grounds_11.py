import csv
import json


def sports_grounds():
    with open('playgrounds.csv', 'r', encoding='UTF-8') as file:
        data = file.read()
        rows = [r.split(';') for r in data.splitlines()]
        del rows[0]

        dict_with_adm_area_and_other = {}

        for row in rows:
            adm_area = row[1]
            district = row[2]
            address = row[3]

            if adm_area not in dict_with_adm_area_and_other:
                dict_with_adm_area_and_other[adm_area] = {district: [address]}
            else:
                if district in dict_with_adm_area_and_other[adm_area]:
                    dict_with_adm_area_and_other[adm_area][district].append(address)
                else:
                    dict_with_adm_area_and_other[adm_area][district] = [address]

    with open('addresses.json', 'w', encoding='UTF-8') as output:
        output.write(json.dumps(dict_with_adm_area_and_other, indent=3, ensure_ascii=False))


sports_grounds()
