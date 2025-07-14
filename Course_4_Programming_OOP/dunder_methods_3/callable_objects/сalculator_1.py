class Calculator:
    def __call__(self, a, b, operation):
        if operation == '/' and b == 0:
            raise ValueError('Деление на ноль невозможно')
        else:
            return eval(f"{a}{operation}{b}")
