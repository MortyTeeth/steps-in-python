def is_fraction(string):
    if len(string) != 0:
        if string.count('/') == 1:
            nums = string.split('/')
            try:
                x = int(nums[0])
                y = int(nums[1])
                if y <= 0:
                    return False
                else:

                    return True
            except:
                return False
        else:
            return False
    else:
        return False
