def sorting_lists(kol):
    l = []
    for i in range(kol):
        spisok = [int(c) for c in input().split()]
        spisok.sort()
        l.extend(spisok)
    l.sort()
    return l


kol = int(input())

print(*sorting_lists(kol))