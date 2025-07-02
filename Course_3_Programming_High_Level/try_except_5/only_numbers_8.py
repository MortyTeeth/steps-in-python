import sys


def only_numbers(rows):
    total = 0
    counter_not_int = 0
    for row in rows:
        try:
            float_row = float(row)
            total += float_row
        except:
            counter_not_int += 1

    if total % 1 == 0:
        print(int(total))
    else:
        print(float(total))
    print(counter_not_int)


rows = [i.strip() for i in sys.stdin]
only_numbers(rows)
