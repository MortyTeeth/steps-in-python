def correct_bracket_sequence(brackets):
    balance = 0
    for bracket in brackets:
        if bracket == '(':
            balance += 1
        elif bracket == ')':
            balance -= 1
        else:
            return False
        if balance < 0:
            return False
    return balance == 0