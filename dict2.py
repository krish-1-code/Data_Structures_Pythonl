import string

ascii = [ord('A')]
print(ascii)

a = "isc"
b = "isc"

print(a == b)

words = ["apple","ball","cat","apple","apple","ball"]
wording = "apple ball cat apple apple ball ball cat ball"

new_wording = wording.split()

print(new_wording)

new_word = { }
counter = 1

for words in new_wording:
    if words not in new_word:
        new_word.update({words : counter})
    else:
        new_word.update({words : new_word[words]+1})

for keys,values in new_word.items():
    print(f"{keys} : {values}")
