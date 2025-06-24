def counter_of_correct_decisions(total_num):
    count_correct = 0
    matrix_with_nickname_and_result = []
    who_solved_task_correctly = set()

    if total_num == 0:
        print('Вы можете стать первым, кто решит эту задачу')
    else:
        for i in range(total_num):
            nickname_and_result = input()
            matrix_with_nickname_and_result.append(nickname_and_result)

        for k in range(total_num):
            if 'Correct' in matrix_with_nickname_and_result[k]:
                count_correct += 1

        for l in range(total_num):
            if 'Correct' in matrix_with_nickname_and_result[l]:
                who_solved_task_correctly.add(matrix_with_nickname_and_result[l])



        if count_correct == 0:
            print('Вы можете стать первым, кто решит эту задачу')
        else:
            how_much_solved_task_correctly = len(who_solved_task_correctly)

            percent_correctly = int(round((count_correct / total_num) * 100 + 0.5, 2))

            print('Верно решили', how_much_solved_task_correctly, 'учащихся')
            print('Из всех попыток ', percent_correctly, '% верных', sep='')


total_number_of_attempts_to_solve_the_problem = int(input())

counter_of_correct_decisions(total_number_of_attempts_to_solve_the_problem)