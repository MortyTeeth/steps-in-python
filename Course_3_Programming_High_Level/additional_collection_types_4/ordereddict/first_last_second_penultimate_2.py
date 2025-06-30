from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

new_dict = OrderedDict()
keys = list(data.keys())
n = len(keys)

for i in range((n + 1) // 2):
    new_dict[keys[i]] = data[keys[i]]
    if i != n - i - 1:
        new_dict[keys[n - i - 1]] = data[keys[n - i - 1]]

print(new_dict)