def filter_anagrams(word, words):
    anagrams = [str(i) for i in word]
    after_comparison = []
    for i in words:
        vr = [str(k) for k in i]
        if sorted(anagrams) == sorted(vr):
            after_comparison.append(i)
    return after_comparison
