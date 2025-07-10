class User:
    def __init__(self, name, age):
        try:
            if name.isalpha() == True and len(name) > 1:
                self._name = name
            else:
                raise ValueError('Некорректное имя')
        except:
            raise ValueError('Некорректное имя')

        try:
            if age < 0 or age > 110 or type(age) != int:
                raise ValueError('Некорректный возраст')
            else:
                self._age = age
        except:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        try:
            if new_name.isalpha() == True and len(new_name) > 1:
                self._name = new_name
            else:
                raise ValueError('Некорректное имя')
        except:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        try:
            if new_age < 0 or new_age > 110 or type(new_age) != int:
                raise ValueError('Некорректный возраст')
            else:
                self._age = new_age
        except:
            raise ValueError('Некорректный возраст')
