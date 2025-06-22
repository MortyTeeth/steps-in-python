def morse_code(txt):
    letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
             '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
             '...--', '....-', '.....', '-....', '--...', '---..', '----.']

    letters_and_morse = dict(zip(letters, morse))

    for i in range(len(txt)):
        if txt[i] in letters_and_morse.keys():
            print(letters_and_morse[txt[i]], end=' ')


text = input().upper()

morse_code(text)
