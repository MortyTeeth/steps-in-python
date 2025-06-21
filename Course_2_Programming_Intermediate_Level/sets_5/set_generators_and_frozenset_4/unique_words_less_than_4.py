sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

punctuation_marks = '.,;:-?!()'
text_after_corrections = ''
final_text = []
for i in range(len(sentence)):
    if sentence[i] not in punctuation_marks:
        text_after_corrections += sentence[i]

text_after_lower = text_after_corrections.lower()
list_after_all = text_after_lower.split()
final_set = set(list_after_all)

converted = text_after_corrections.split()

for i in range(len(converted)):
    if len(converted[i]) < 4:
        final_text.append(converted[i].lower())

final_final_set = set(final_text)
print(*sorted(final_final_set))
