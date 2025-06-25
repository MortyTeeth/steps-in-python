def correct_IP_address(string):
    num_for_check = []
    for num in string:
        if num.isdigit() and 0 <= int(num) <= 255:
            num_for_check.append(int(num))
        else:
            return False
    for num in num_for_check:
        if 0 <= num <= 255:
            return True
        else:
            return False


string = input().split('.')
print(correct_IP_address(string))
