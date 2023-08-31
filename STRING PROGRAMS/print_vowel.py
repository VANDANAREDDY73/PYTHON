S = 'AVENGERS'
newStr = ''
for ch in S:
    if ch in 'aeiouAEIOU':
        newStr += ch
print(newStr)
