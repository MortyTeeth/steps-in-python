class TitledText(str):
    def __new__(cls, content, text_title):
        content = super().__new__(cls, content)
        content.text_title = text_title
        return content

    def __init__(self, content, text_title):
        self.content = content
        self.text_title = text_title

    def title(self):
        return self.text_title
