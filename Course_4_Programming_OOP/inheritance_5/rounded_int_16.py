class RoundedInt(int):
    def __new__(cls, num, even=True):
        if num % 2 != 0 and even == True:
            return super().__new__(cls, num + 1)
        elif num % 2 == 0 and even == True:
            return super().__new__(cls, num)
        elif num % 2 != 0 and even == False:
            return super().__new__(cls, num)
        elif num % 2 == 0 and even == False:
            return super().__new__(cls, num + 1)

        return super().__new__(cls)

    def __init__(self, num, even=True):
        pass
