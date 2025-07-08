from itertools import product


def password_gen():
    for password in product(range(10), range(10), range(10)):
        yield str(password[0]) + str(password[1]) + str(password[2])
