def check_the_nickname(nick):
    if 5 <= len(nick) <= 15 and nick[0] == '@' and all(char.isdigit() or 'a' <= char <= 'z' for char in nick[1:]):
        print('Correct')
    else:
        print('Incorrect')


nickname = input()
check_the_nickname(nickname)