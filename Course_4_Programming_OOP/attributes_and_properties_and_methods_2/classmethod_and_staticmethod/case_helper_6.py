class CaseHelper:
    def __init__(self):
        pass

    @staticmethod
    def is_snake(string):
        count_ = string.count('_')
        split_string = string.split('_')
        count = 0
        for word in split_string:
            if word.islower():
                count += 1
            else:
                return False

        if count_ == count - 1:
            return True
        else:
            return False

    @staticmethod
    def is_upper_camel(string):
        if string[0].isupper() and string.isalpha():
            return True
        else:
            return False

    @staticmethod
    def to_snake(string):
        second_string = ''
        for i in string:
            if i.isupper():
                second_string += '_' + i
            else:
                second_string += i
        if second_string[0] == '_':
            second_string = second_string[1:]
        else:
            pass
        second_string = second_string.lower()
        return second_string

    @staticmethod
    def to_upper_camel(string):
        string_split = string.split('_')
        second_list = []
        for word in string_split:
            sec_string = ''
            for char in range(len(word)):
                if char == 0:
                    sec_string += word[char].upper()
                else:
                    sec_string += word[char]
            second_list.append(sec_string)

        return ''.join(second_list)
