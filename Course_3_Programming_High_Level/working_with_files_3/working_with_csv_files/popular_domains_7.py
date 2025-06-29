import csv


def popular_domains():
    with open('data.csv', 'r', encoding='UTF-8') as file, open('domain_usage.csv', 'w', newline='',
                                                               encoding='UTF-8') as domain:
        rows = csv.reader(file)
        list_with_email = []
        for row in rows:
            list_with_email.append(row[2])
        del list_with_email[0]

        new_list = [r.split('@') for r in list_with_email]

        dict_with_domain_and_counts = dict()

        for value in new_list:
            if value[1] not in dict_with_domain_and_counts:
                dict_with_domain_and_counts.update({value[1]: 1})
            else:
                dict_with_domain_and_counts.update({value[1]: dict_with_domain_and_counts[value[1]] + 1})

        sorted_dict = dict(sorted(dict_with_domain_and_counts.items(), key=lambda x: (x[1], x[0])))

        columns = ['domain', 'count']

        writer = csv.DictWriter(domain, fieldnames=columns, delimiter=',')
        writer.writeheader()
        for row in sorted_dict:
            writer.writerow({'domain': row, 'count': sorted_dict[row]})


popular_domains()
