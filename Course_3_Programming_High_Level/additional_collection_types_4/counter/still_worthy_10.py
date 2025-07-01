from collections import Counter
import sys

c = Counter()
for data in sys.stdin:
    name, score = data.split()
    c.update({name: int(score)})
print(c.most_common()[-2][0])
