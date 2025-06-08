def is_one_away(word1, word2):
    count = 0
    if word1 == word2:
        return False
    elif len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
        if count == len(word1) or count - 1 == len(word1) or count == len(word1) - 1:
            return True
        else:
            return False
    else:
        return False
    pass


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))
