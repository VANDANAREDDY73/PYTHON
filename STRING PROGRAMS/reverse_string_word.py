#reverse string without reversing words
S = 'we are in class room'
L = S.split()
newList = L[::-1]
print(' '.join(newList))

#without using in-built methods
S = 'we are in class room'
word,res = '',''
for ch in S:
    if ch == ' ':
        res = ' '+word+res
        word = ''
    else:
        word = word+ch
print(word+res)
