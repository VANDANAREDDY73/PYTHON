S = 'ashdsbcvahsd'
L = []
string = ''
for char in S:
    if char not in string:
        string += char
    else:
        L.append(string)
        string = char
L.append(string)
print(L)
hl = 0
high_length_word = ''
for word in L:
    if len(word) > hl:
        hl = len(word)
        high_length_word = word
print(high_length_word)


