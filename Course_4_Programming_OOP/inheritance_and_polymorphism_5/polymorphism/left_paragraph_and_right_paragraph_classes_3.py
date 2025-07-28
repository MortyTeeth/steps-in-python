from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length):
        self.length = length
        self.lines = [[]]
        self.current_length = 0

    def add(self, text):
        words = text.split()
        for word in words:
            word_length = len(word)
            if self.current_length + (1 if self.current_length > 0 else 0) + word_length > self.length:
                self.lines.append([word])
                self.current_length = word_length
            else:
                if self.current_length > 0:
                    self.current_length += 1
                self.lines[-1].append(word)
                self.current_length += word_length

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        for line in self.lines:
            print(' '.join(line))
        self.lines = [[]]
        self.current_length = 0


class RightParagraph(Paragraph):
    def end(self):
        for line in self.lines:
            text = ' '.join(line)
            padding = self.length - len(text)
            print(' ' * padding + text)
        self.lines = [[]]
        self.current_length = 0
