def good_password(password):
    if all([len(password) >= 7, any(symbol.isdigit() for symbol in password),
            any(symbol.isupper() for symbol in password), any(symbol.islower() for symbol in password)]):
        return 'YES'
    else:
        return 'NO'


password = input()

print(good_password(password))
