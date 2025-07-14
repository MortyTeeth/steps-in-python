class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        self.first_string = ''
        flag = True
        for char in range(len(string)):
            if string[char] in self.chars and flag == True:
                pass
            elif string[char] in self.chars and flag == False:
                self.first_string += string[char]
            else:
                self.first_string += string[char]
                flag = False

        flag = True
        self.second_string = ''.join([str(i) for i in reversed(self.first_string)])
        self.end_string = ''
        for char in range(len(self.second_string)):
            if self.second_string[char] in self.chars and flag == True:
                pass
            elif self.second_string[char] in self.chars and flag == False:
                self.end_string += self.second_string[char]
            else:
                self.end_string += self.second_string[char]
                flag = False

        return ''.join([str(i) for i in reversed(self.end_string)])
