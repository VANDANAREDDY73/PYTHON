#reverse words in string without reversing string
S = 'we are in class room'
L = S.split()
newList = []
for word in L:
    newList.append(word[::-1])
print(' '.join(newList))

#without using in-built methods
S = 'we are in class room'
word,res = '',''
for ch in S:
    if ch == ' ':
        res = res+word+' '
        word = ''
    else:
        word = ch + word
print(res+word)
