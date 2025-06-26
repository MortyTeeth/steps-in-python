from datetime import *

with open('logfile.txt', 'r', encoding='utf-8') as logfile, open('output.txt', 'w', encoding='utf-8') as output:
    all_data = [i.rstrip() for i in logfile.readlines()]
    dict_with_data = dict()

    for data in all_data:
        dict_with_data.update({data.split(', ')[0]: [data.split(', ')[1], data.split(', ')[2]]})

    for key, value in dict_with_data.items():
        time1 = value[0]
        time2 = value[1]
        format = "%H:%M"
        entry_time = datetime.strptime(time1, format)
        output_time = datetime.strptime(time2, format)

        time_difference = output_time - entry_time

        if time_difference.total_seconds() / 60 >= 60:
            print(key.rstrip())
