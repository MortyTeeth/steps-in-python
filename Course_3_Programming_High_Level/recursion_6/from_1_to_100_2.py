def from_1_to_100(num):
    if num <= 100:
        print(num)
        from_1_to_100(num + 1)


from_1_to_100(1)
