files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']
png = '.png'
text_after_corrections = ''
final_text = []
for i in range(len(files)):
    if png in files[i].lower():
        final_text.append(files[i].lower())

final_set = set(final_text)
print(*sorted(final_set))
