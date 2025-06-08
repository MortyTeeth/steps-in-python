def correct_bracket_sequence(brackets):
    list_with_brackets = [i for i in brackets]
    quantity_left_brackets = 0
    quantity_right_brackets = 0
    for bracket in list_with_brackets:
        if bracket == '(':
            quantity_left_brackets += 1
        else:
            quantity_right_brackets += 1
        if quantity_right_brackets > quantity_left_brackets:
            return 'False'
    if quantity_right_brackets != quantity_left_brackets:
        return 'False'
    return 'True'


brackets = input()
print(correct_bracket_sequence(brackets))
