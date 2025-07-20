class HtmlTag:
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        self.line = ''

    def __enter__(self):
        HtmlTag.level += 1
        if self.inline:
            self.line = f"<{self.tag}>"
        else:
            print('  ' * HtmlTag.level + f"<{self.tag}>")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.inline:
            self.line += f"</{self.tag}>"
            print('  ' * HtmlTag.level + self.line)
        else:
            print('  ' * HtmlTag.level + f"</{self.tag}>")
        HtmlTag.level -= 1

    def print(self, text):
        if self.inline:
            self.line += text
        else:
            print('  ' * (HtmlTag.level + 1) + text)


HtmlTag.level = -1
