import csv
import json


def students_of_the_course():
    with open('students.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        list_with_completed_students = []

        for student in data:
            if student['age'] >= 18 and student['progress'] >= 75:
                list_with_completed_students.append(student)

        sorted_list = sorted(list_with_completed_students, key=lambda x: x['name'])

    with open('data.csv', 'w', encoding='UTF-8', newline='') as output:
        writer = csv.DictWriter(output, fieldnames=['name', 'phone'], delimiter=',')
        writer.writeheader()
        for row in sorted_list:
            writer.writerow({'name': row['name'], 'phone': row['phone']})


students_of_the_course()
