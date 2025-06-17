def competitive_selection(num):
    students = []
    for i in range(num):
        last_name_and_rating = input().split()
        student_last_name = last_name_and_rating[0]
        rating = last_name_and_rating[1]
        tup = student_last_name, rating
        students.append(tup)

    for k in range(len(students)):
        print(*students[k])

    print()

    for l in range(len(students)):
        if int(students[l][1]) >= 4:
            print(*students[l])


number_of_student = int(input())

competitive_selection(number_of_student)
