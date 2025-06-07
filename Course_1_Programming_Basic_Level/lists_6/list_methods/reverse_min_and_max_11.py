s = input()

a = s.split()

news = []

ss = []

for i in range(len(a)):
    news.append(int(a[i]))

positionmax = news.index(max(news))
positionmin = news.index(min(news))

m = max(news)
mi = min(news)

del news[positionmax]
news.insert(positionmax, mi)
del news[positionmin]
news.insert(positionmin, m)

for j in range(len(news)):
    ss.append(str(news[j]))

sss = ' '.join(ss)
print(sss)