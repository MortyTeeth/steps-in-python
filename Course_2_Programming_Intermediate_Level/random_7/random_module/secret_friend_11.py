def secret_friend(num):
    first_list = []

    for i in range(num):
        name = input()
        first_list.append(name)

    second_list = first_list.copy()

    second_list[0] = first_list[-1]
    second_list[1:] = first_list[0:-1]

    for k in range(len(second_list)):
        print(first_list[k] + ' - ' + second_list[k])


number_friends = int(input())

secret_friend(number_friends)
