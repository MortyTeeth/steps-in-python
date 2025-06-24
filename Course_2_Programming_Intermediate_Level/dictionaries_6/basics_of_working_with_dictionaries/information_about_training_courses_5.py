def information_about_training_courses(string):
    info = [{'course number': 'CS101', 'audience number': 3004, 'teacher': 'Хайнс', 'time': '8:00'},
            {'course number': 'CS102', 'audience number': 4501, 'teacher': 'Альварадо', 'time': '9:00'},
            {'course number': 'CS103', 'audience number': 6755, 'teacher': 'Рич', 'time': '10:00'},
            {'course number': 'NT110', 'audience number': 1244, 'teacher': 'Берк', 'time': '11:00'},
            {'course number': 'CM241', 'audience number': 1411, 'teacher': 'Ли', 'time': '13:00'}]

    for i in range(len(info)):
        if string in info[i]['course number']:
            print(string, ': ', info[i]['audience number'], ', ', info[i]['teacher'], ', ', info[i]['time'], sep='')


string = input()

information_about_training_courses(string)
