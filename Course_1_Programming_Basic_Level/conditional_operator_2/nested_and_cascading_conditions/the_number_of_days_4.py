month_number = int(input())

if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
    print(31)
elif month_number == 2:
    print(28)
else:
    print(30)